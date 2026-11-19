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
* `TLDR` (Text)
* `Konferencja` (Select)
* `Rok` (Number)
* `PDF` (URL)
* `Repo` (URL)
* `Zastosowanie` (Multi-select)
* `Moja Ocena` (Select)
* `Tagi` (Multi-select)
* `Afiliacja` (Multi-select)


2. **Configure API Access:**
* Create an internal integration at [notion.so/profile/integrations](https://www.notion.so/profile/integrations) and connect it to the page containing **`Baza Wiedzy NLP`** (`•••` → **Connections**).
* Create and fill `.env` file in the project root

## Usage

* **Initialize a new conference folder:**
```bash
./scripts/init_conf.sh ACL27

```

* **Generate notes in `agy`:**
* Posters: `Use poster-note skill for EMNLP26`
* Single article/paper: `Use link-note skill for https://arxiv.org/abs/...`
