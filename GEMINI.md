# Kontekst: Baza Wiedzy NLP

## Profil i cel
Baza notatek z publikacji naukowych, artykułów i posterów konferencyjnych. Cel: wyciągnięcie głównych wniosków i ocena łatwości zastosowania technik w moich dwóch obszarach:
1. **Post-training LLM (PL):** SFT, kuracja danych, ewaluacja, transfer międzyjęzykowy. Preferuję techniki niewymagające przebudowy architektury czy pisania pipeline'ów od zera (np. zmiana funkcji straty, triki treningowe/danowe, ewaluacja). Prace wymagające głębszych zmian nadal są cenne ze względu na same wnioski.
2. **Interpretowalność i sterowanie LLM:** Sparse Autoencoders (SAE), Mechanistic Interpretability, steering. Interesują mnie detale treningu SAE, jakość reprezentacji, auto-interp oraz stabilność sterowania.

## Schemat danych dla Notion (`Baza Wiedzy NLP`)
Właściwości przekazywane do skryptu `scripts/save_to_notion.py`:
- `tytul` – pełny tytuł publikacji lub artykułu
- `tldr_short` – jedno bardzo krótkie zdanie (maks. 12-15 słów) do wyświetlenia w tabeli: co to dokładnie jest (np. "Metoda filtrowania danych SFT oparta na niepewności modelu bazowego" albo "Benchmark ewaluacji SAE na zadaniach sterowania").
- `konferencja` – nazwa folderu (np. `"EMNLP26"`) lub `null` dla pojedynczych linków
- `rok` – rok publikacji jako liczba (np. `2026`)
- `afiliacja` – lista głównych uczelni/firm autorów (**uwaga: bez przecinków wewnątrz nazw**, bo to pole Multi-select)
- `pdf` – link do publikacji (arXiv / ACL Anthology / artykuł) lub `null`
- `repo` – link do kodu lub danych (tylko jeśli podany w treści pracy) lub `null`
- `tagi` – lista zwięzłych tagów po angielsku (np. `SFT`, `Data-Curation`, `Loss-Function`, `Evaluation`, `Multilingual`, `SAE`, `Steering`, `MechInterp`)
- `zastosowanie` – wybierz 1 (max 2) opcję z listy:
  - `Wniosek` – cenna obserwacja empiryczna lub wskazówka, którą warto mieć w pamięci
  - `Test` – konkretna technika/metoda warta przetestowania w moich projektach
  - `Teoria` – praca czysto teoretyczna, mało praktyczna (trudna i specyficzna) w bezpośrednim wdrożeniu
  - `Produkt` – gotowe narzędzie, biblioteka, model lub benchmark udostępniony do użycia
  - `Tajne` – firma po prostu chwali się produktem, którego sam nie użyję, brak szczegółów implementacyjnych

**Zasady krytyczne:**
- Zapisu do Notion dokonuj **wyłącznie** przez skrypt `uv run scripts/save_to_notion.py` (nie używaj narzędzi Notion MCP do tworzenia stron).
- Nigdy nie zgaduj ani nie wymyślaj adresów URL.