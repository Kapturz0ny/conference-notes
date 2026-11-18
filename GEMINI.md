# Kontekst: Baza Wiedzy NLP

## Profil i cel
Baza notatek z publikacji naukowych, artykułów i posterów konferencyjnych. Cel: wyciągnięcie głównych wniosków i ocena łatwości zastosowania technik w moich dwóch obszarach:
1. **Post-training LLM (PL):** SFT, kuracja danych, ewaluacja, transfer międzyjęzykowy. Preferuję techniki niewymagające przebudowy architektury czy pisania pipeline'ów od zera (np. zmiana funkcji straty, triki treningowe/danowe, ewaluacja). Prace wymagające głębszych zmian nadal są cenne ze względu na same wnioski.
2. **Interpretowalność i sterowanie LLM:** Sparse Autoencoders (SAE), Mechanistic Interpretability, steering. Interesują mnie detale treningu SAE, jakość reprezentacji, auto-interp oraz stabilność sterowania.

## Baza Notion: `Baza Wiedzy NLP`
Właściwości do uzupełnienia przez agenta:
- `Tytuł` (Title) – pełny tytuł publikacji lub artykułu
- `Konferencja` (Select) – nazwa folderu (np. `EMNLP26`); **zostaw puste** przy pojedynczych linkach spoza konferencji
- `Rok` (Number) – rok publikacji (np. `2026`)
- `Afiliacja` (Multi-select) – główne uczelnie/firmy autorów
- `PDF` (URL) – link do publikacji (arXiv / ACL Anthology / artykuł)
- `Repozytorium` (URL) – link do kodu lub danych (tylko jeśli podany w treści pracy)
- `Tagi` (Multi-select) – napisz odpowiednie tagi tematyczne (np. `SFT`, `Data-Curation`, `Loss-Function`, `Evaluation`, `Multilingual`, `SAE`, `Steering`, `MechInterp`)

**Zasady krytyczne:**
- **NIE uzupełniaj** pola `Przydatność` – zostaw je zawsze puste (wypełniam je ręcznie).