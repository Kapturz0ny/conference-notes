# Conference & Research Notes Agent

Automated workflow for turning conference poster photos and research links into structured Notion notes using Google Antigravity (`agy`).

## Setup

Install system dependency (`libzbar0` for QR decoding) and Python environment via `uv`:

```bash
sudo apt update && sudo apt install -y libzbar0
uv sync
```

## Notion Integration

1. **Create a Notion Database:** Create an inline database named **`Baza Wiedzy NLP`** with the following properties:
* `Tytuł` (Title)
* `Konferencja` (Select)
* `Rok` (Number)
* `Afiliacja` (Multi-select)
* `PDF` (URL)
* `Repozytorium` (URL)
* `Tagi` (Multi-select)
* `Przydatność` (Select)


2. **Connect Notion MCP in `agy`:**
```bash
agy mcp add notion [https://mcp.notion.com/mcp](https://mcp.notion.com/mcp)
```

Launch `agy`, run `/mcp`, select `notion`, and complete OAuth in your browser granting access to the page containing **`Baza Wiedzy NLP`**.
