import json
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

def upload_image(notion: Client, image_path: Path) -> str | None:
    if not image_path or not image_path.exists():
        return None
    mime = "image/png" if image_path.suffix.lower() == ".png" else "image/jpeg"
    upload = notion.file_uploads.create(
        mode="single_part",
        filename=image_path.name,
        content_type=mime,
    )
    with open(image_path, "rb") as f:
        notion.file_uploads.send(file_upload_id=upload["id"], file=f)
    return upload["id"]

def get_data_source_id(notion: Client, db_id: str) -> str:
    db = notion.databases.retrieve(database_id=db_id)
    data_sources = db.get("data_sources", [])
    if not data_sources:
        raise ValueError(f"No data sources found for database {db_id}")
    return data_sources[0]["id"]

def is_duplicate(notion: Client, db_id: str, title: str, pdf_url: str | None) -> bool:
    filters = [{"property": "Tytuł", "title": {"equals": title}}]
    if pdf_url:
        filters.append({"property": "PDF", "url": {"equals": pdf_url}})
    res = notion.request(
        path=f"databases/{db_id}/query",
        method="POST",
        body={"filter": {"or": filters}},
    )
    return len(res.get("results", [])) > 0

def text_blocks(items: list[str]) -> list[dict]:
    blocks = []
    for item in items:
        # Notion ma limit 2000 znaków na jeden blok tekstu
        for i in range(0, len(item), 1950):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"type": "text", "text": {"content": item[i:i+1950]}}]
                },
            })
    return blocks

def h2(title: str) -> dict:
    return {
        "object": "block",
        "type": "heading_2",
        "heading_2": {"rich_text": [{"type": "text", "text": {"content": title}}]},
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: uv run scripts/save_to_notion.py <path_to_note.json>")
        sys.exit(1)

    json_path = Path(sys.argv[1])
    data = json.loads(json_path.read_text(encoding="utf-8"))

    notion = Client(auth=os.environ["NOTION_TOKEN"], notion_version="2022-06-28")
    db_id = os.environ["NOTION_DATABASE_ID"]
    data_source_id = get_data_source_id(notion, db_id)

    title = data["tytul"].strip()
    pdf_url = data.get("pdf") or None

    if is_duplicate(notion, data_source_id, title, pdf_url):
        print(f"SKIPPED (duplicate in Notion): {title}")
        return

    props = {
        "Tytuł": {"title": [{"text": {"content": title}}]},
        "TLDR": {"rich_text": [{"text": {"content": data.get("tldr_short", "")[:2000]}}]},
        "Tagi": {"multi_select": [{"name": t} for t in data.get("tagi", [])]},
        "Zastosowanie": {"multi_select": [{"name": z} for z in data.get("zastosowanie", [])]},
    }
    if data.get("konferencja"):
        props["Konferencja"] = {"select": {"name": data["konferencja"]}}
    if data.get("rok"):
        props["Rok"] = {"number": int(data["rok"])}
    if data.get("afiliacja"):
        props["Afiliacja"] = {"multi_select": [{"name": a} for a in data["afiliacja"]]}
    if pdf_url:
        props["PDF"] = {"url": pdf_url}
    if data.get("repo"):
        props["Repo"] = {"url": data["repo"]}

    children = []

    img_str = data.get("image_path")
    if img_str:
        upload_id = upload_image(notion, Path(img_str))
        if upload_id:
            children.append({
                "object": "block",
                "type": "image",
                "image": {"type": "file_upload", "file_upload": {"id": upload_id}},
            })

    children.append(h2("TL;DR"))
    children.append({
        "object": "block",
        "type": "paragraph",
        "paragraph": {"rich_text": [{"type": "text", "text": {"content": data.get("tldr", "")[:1950]}}]},
    })

    children.append(h2("Zastosowanie i ocena praktyczna"))
    children.extend(text_blocks(data.get("ocena_praktyczna", [])))

    children.append(h2("Key Takeaways"))
    children.extend(text_blocks(data.get("key_takeaways", [])))

    children.append(h2("Linki i źródła"))
    children.extend(text_blocks(data.get("linki_i_zrodla", [])))

    notion.pages.create(parent={"database_id": db_id}, properties=props, children=children)
    print(f"SAVED TO NOTION: {title}")

if __name__ == "__main__":
    main()
