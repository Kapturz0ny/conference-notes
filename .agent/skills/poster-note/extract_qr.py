import sys
import json
from pathlib import Path
import cv2
from pyzbar.pyzbar import decode

def scan_region(img):
    urls = set()
    for obj in decode(img):
        urls.add(obj.data.decode("utf-8", errors="ignore"))
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 11
    )
    for obj in decode(thresh):
        urls.add(obj.data.decode("utf-8", errors="ignore"))
    return urls

def extract_from_image(image_path: str) -> list[str]:
    img = cv2.imread(image_path)
    if img is None:
        return []

    found_urls = scan_region(img)
    h, w, _ = img.shape
    mid_h, mid_w = int(h * 0.55), int(w * 0.55)
    crops = [
        img[0:mid_h, 0:mid_w],
        img[0:mid_h, w - mid_w:w],
        img[h - mid_h:h, 0:mid_w],
        img[h - mid_h:h, w - mid_w:w],
    ]
    for crop in crops:
        found_urls.update(scan_region(crop))

    return sorted(list(found_urls))

def get_processed_files(target: Path) -> set[str]:
    posters_dir = target.parent if target.is_file() else target
    processed_file = posters_dir.parent / "processed.json"
    if not processed_file.exists():
        return set()
    try:
        data = json.loads(processed_file.read_text(encoding="utf-8"))
        processed = set()
        for item in data:
            if isinstance(item, str):
                processed.add(item)
            elif isinstance(item, dict) and "file" in item:
                processed.add(item["file"])
        return processed
    except Exception:
        return set()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: uv run extract_qr.py <path_to_dir_or_file>")
        sys.exit(1)

    target = Path(sys.argv[1])
    processed = get_processed_files(target)
    results = {}
    exts = {".jpg", ".jpeg", ".png", ".webp"}

    files = [target] if target.is_file() else [
        p for p in sorted(target.iterdir())
        if p.is_file() and p.suffix.lower() in exts and p.name not in processed
    ]

    for f in files:
        results[f.name] = extract_from_image(str(f))

    print(json.dumps(results, indent=2, ensure_ascii=False))