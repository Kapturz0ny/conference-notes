---
name: poster-note
description: Kadruje zdjęcia posterów, odczytuje kody QR, analizuje treść i tworzy notatki w Notion.
---

# Procedura dla wskazanego folderu konferencji (np. `EMNLP26`)

1. **Inwentaryzacja:**
   - Pobierz obrazy z `<folder>/posters/` i odfiltruj wszystkie pliki obecne już w `<folder>/processed.json` (chyba że użytkownik jawnie poprosi o przetworzenie plików ze statusem `"needs_argon"`).
   - Przy >5 zdjęciach do przetworzenia podziel pracę na partie po 5 sztuk dla subagentów.

2. **Kadrowanie i ekstrakcja QR:**
   - Przytnij i wyprostuj każdy poster (współrzędne `0-1000`):
     - Zdjęcie na wprost: `uv run .agent/skills/poster-note/process_image.py <plik> <ymin> <xmin> <ymax> <xmax>`
     - Zdjęcie pod kątem (4 rogi: `tl_y tl_x tr_y tr_x br_y br_x bl_y bl_x`): `uv run .agent/skills/poster-note/process_image.py <plik> <8_współrzędnych>`
   - Odczytaj kody QR:
     - Dla całego folderu: `uv run .agent/skills/poster-note/extract_qr.py <folder>/posters/`
     - Dla pojedynczego pliku (np. z `needs_argon`): `uv run .agent/skills/poster-note/extract_qr.py <folder>/posters/<plik>`
   - Jeśli QR prowadzi do strony projektu lub skracacza, otwórz ten adres, aby wyciągnąć bezpośrednie linki do PDF i repozytorium.

3. **Analiza (rygorystyczne źródła i routing):**
   - **Jeśli pracujesz jako model Hydrogen:** oceń złożoność postera. Jeśli praca jest bardzo gęsta matematycznie, zawiera skomplikowane dowody lub głęboką analizę mechanistyczną (np. zaawansowane SAE) wymagającą głębszego rozumowania, **nie zapisuj jej w Notion** – dopisz plik do `<folder>/processed.json` jako `{"file": "<nazwa>", "status": "needs_argon"}` i przejdź dalej.
   - Bazuj **głównie na treści postera** (tytuł, autorzy, afiliacje, metodyka, wykresy, liczby).
   - **Kiedy wolno sięgnąć do publikacji z sieci:** tylko wtedy, gdy na posterze jest QR/link **LUB** gdy fragment postera jest zasłonięty, ale wyraźnie widać **pełny tytuł oraz nazwiska autorów**.
   - Nieczytelne zdjęcia zapisz w `processed.json` jako `{"file": "<nazwa>", "status": "skipped"}`.

4. **Zapis w Notion:**
   - Zapisz wynik analizy do unikalnego pliku `/tmp/note/note_<nazwa_pliku>.json` zgodnie z zasadami z `GEMINI.md`:
     ```json
     {
       "tytul": "Pełny tytuł z postera",
       "konferencja": "EMNLP26",
       "rok": 2026,
       "afiliacja": ["Uczelnia 1", "Firma 2"],
       "pdf": "https://...",
       "repo": null,
       "tagi": ["Tag1", "Tag2"],
       "zastosowanie": ["Wniosek", "Test"],
       "image_path": "EMNLP26/posters/cropped/plik.jpg",
       "tldr": "Maksymalnie 3 zdania: problem, metoda, główny wynik.",
       "ocena_praktyczna": [
         "Ocena pod profil z GEMINI.md: co konkretnie można wykorzystać...",
         "Nakład zmian w pipeline/architekturze oraz główne ograniczenia..."
       ],
       "key_takeaways": [
         "Detale techniczne, modele, datasety...",
         "Konkretne wyniki liczbowe z posteru..."
       ],
       "linki_i_zrodla": [
         "Publikacja: https://...",
         "Autorzy: Imię Nazwisko, ..."
       ]
     }
     ```
   - Wyślij notatkę do Notion uruchamiając:
     `uv run scripts/save_to_notion.py /tmp/note/note_<nazwa_pliku>.json`

5. **Rejestr:**
   - Po udanym zapisie w Notion dopisz do `<folder>/processed.json` wpis `{"file": "<nazwa>", "status": "done"}` (jeśli plik miał wcześniej status `"needs_argon"`, zaktualizuj go na `"done"`).
