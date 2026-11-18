---
name: poster-note
description: Kadruje zdjęcia posterów, odczytuje kody QR, analizuje treść i tworzy notatki w Notion.
---

# Procedura dla wskazanego folderu konferencji (np. `EMNLP26`)

1. **Inwentaryzacja:**
   - Pobierz obrazy z `<folder>/posters/` i odfiltruj wszystkie pliki obecne już w `<folder>/processed.json` (niezależnie od statusu: `"done"`, `"skipped"`, `"needs_argon"`).
   - Przy >5 nowych zdjęciach podziel pracę na partie po 5 sztuk dla subagentów.

2. **Kadrowanie i ekstrakcja QR:**
   - Przytnij i wyprostuj każdy poster (współrzędne `0-1000`):
     - Jeśli zdjęcie jest na wprost: `uv run .agent/skills/poster-note/process_image.py <plik> <ymin> <xmin> <ymax> <xmax>`
     - Jeśli zdjęcie jest pod kątem (wymaga wyprostowania perspektywy): podaj 4 rogi arkusza (`tl_y tl_x tr_y tr_x br_y br_x bl_y bl_x`): `uv run .agent/skills/poster-note/process_image.py <plik> <8_współrzędnych>`
   - Odczytaj kody QR z oryginalnych zdjęć:
     `uv run .agent/skills/poster-note/extract_qr.py <folder>/posters/`
   - Jeśli QR prowadzi do strony projektu lub skracacza, otwórz ten adres, aby wyciągnąć bezpośrednie linki do PDF i repozytorium.

3. **Analiza (rygorystyczne źródła i routing):**
   - **Jeśli pracujesz jako model Hydrogen:** oceń złożoność postera. Jeśli praca jest bardzo gęsta matematycznie, zawiera skomplikowane dowody lub głęboką analizę mechanistyczną (np. zaawansowane SAE) wymagającą głębszego rozumowania, **nie zapisuj jej w Notion** – dopisz plik do `<folder>/processed.json` jako `{"file": "<nazwa>", "status": "needs_argon"}` i przejdź do kolejnego zdjęcia.
   - Bazuj **głównie na treści postera** (tytuł, autorzy, afiliacje, metodyka, wykresy, liczby).
   - **Kiedy wolno sięgnąć do publikacji z sieci:** tylko wtedy, gdy na posterze jest QR/link **LUB** gdy fragment postera jest zasłonięty, ale wyraźnie widać **pełny tytuł oraz nazwiska autorów**.
   - Nieczytelne zdjęcia zapisz w `processed.json` jako `{"file": "<nazwa>", "status": "skipped"}`.

4. **Zapis w Notion (`Baza Wiedzy NLP`):**
   - Wypełnij właściwości: `Tytuł`, `Konferencja`, `Rok`, `Afiliacja`, `PDF`, `Repozytorium`, `Tagi`. Pole `Przydatność` zostaw puste.
   - Utwórz treść strony w dokładnej kolejności:
     1. **Zdjęcie postera** (załącz wykadrowany plik z `<folder>/posters/cropped/<nazwa_pliku>` na samej górze strony, przed tekstem).
     2. **TL;DR** (maks. 3 zdania: problem, metoda, wynik).
     3. **Zastosowanie i ocena praktyczna** (ocena pod profil z `GEMINI.md`: co można wykorzystać, nakład zmian w pipeline/architekturze, ograniczenia).
     4. **Key Takeaways** (punktowana lista detali technicznych, modeli, datasetów i konkretnych wyników liczbowych).
     5. **Linki i źródła** (tylko linki z postera/QR oraz lista autorów).

5. **Rejestr:**
   - Po udanym zapisie w Notion dopisz do `<folder>/processed.json` wpis `{"file": "<nazwa>", "status": "done"}` (jeśli plik miał wcześniej status `"needs_argon"`, zaktualizuj go na `"done"`).
