---
name: link-note
description: Tworzy notatkę w Notion na podstawie podanego linku do publikacji (arXiv, PDF) lub artykułu technicznego.
---

# Procedura dla pojedynczego linku (URL)

1. **Pobranie i analiza treści:**
   - Odczytaj treść pod wskazanym adresem URL (jeśli to link `arxiv.org/abs/...`, pobierz pełny tekst z `arxiv.org/pdf/...` lub `ar5iv`, aby dotrzeć do szczegółów metodyki i wyników).
   - Bazuj **wyłącznie na treści tego dokumentu** – nie przeszukuj sieci w poszukiwaniu innych prac. Wyciągnij link do repozytorium (GitHub/HuggingFace) tylko wtedy, gdy autorzy podali go bezpośrednio w tekście.

2. **Przygotowanie i zapis w Notion:**
   - Zapisz wynik analizy do pliku `/tmp/note/note_link.json` zgodnie z zasadami z `GEMINI.md`:
     ```json
     {
       "tytul": "Pełny tytuł pracy",
       "konferencja": null,
       "rok": 2026,
       "afiliacja": ["Uczelnia 1", "Firma 2"],
       "pdf": "https://podany-link...",
       "repo": "[https://github.com/](https://github.com/)..." ,
       "tagi": ["Tag1", "Tag2"],
       "zastosowanie": ["Wniosek", "Test"],
       "image_path": null,
       "tldr": "Maksymalnie 3 zdania: problem, metoda, główny wynik.",
       "ocena_praktyczna": [
         "Ocena pod profil z GEMINI.md: co konkretnie można wykorzystać...",
         "Nakład zmian w pipeline/architekturze oraz główne ograniczenia..."
       ],
       "key_takeaways": [
         "Detale techniczne, modele, datasety...",
         "Konkretne wyniki liczbowe z eksperymentów..."
       ],
       "linki_i_zrodla": [
         "Publikacja: https://...",
         "Repo: https://... (lub brak)",
         "Autorzy: Imię Nazwisko, ..."
       ]
     }
     ```
   - Wyślij notatkę do Notion uruchamiając:
     `uv run scripts/save_to_notion.py /tmp/note/note_link.json`
