---
name: link-note
description: Tworzy notatkę w Notion na podstawie podanego linku do publikacji (arXiv, PDF) lub artykułu technicznego.
---

# Procedura dla pojedynczego linku (URL)

Gdy użytkownik poda link do publikacji, pliku PDF lub artykułu:

1. **Pobranie i analiza treści:**
   - Odczytaj treść pod wskazanym adresem URL (jeśli to link `arxiv.org/abs/...`, możesz pobrać także pełny tekst z `arxiv.org/pdf/...` lub `ar5iv`, aby dotrzeć do szczegółów metodyki i wyników).
   - Bazuj **wyłącznie na treści tego dokumentu** – nie przeszukuj sieci w poszukiwaniu innych prac. Wyciągnij link do repozytorium (GitHub/HuggingFace) tylko wtedy, gdy autorzy podali go bezpośrednio w tekście/abstrakcie.

2. **Zapis w Notion (`Baza Wiedzy NLP`):**
   - Wypełnij właściwości: `Tytuł`, `Rok`, `Afiliacja`, `PDF` (podany link), `Repozytorium` (jeśli znaleziono w tekście), `Tagi`.
   - Pola `Konferencja` oraz `Przydatność` **zostaw puste**.
   - Utwórz treść strony w dokładnej kolejności (bez zdjęcia na górze):
     1. **TL;DR** (maks. 3 zdania: problem, metoda, wynik).
     2. **Zastosowanie i ocena praktyczna** (ocena pod profil z `GEMINI.md`: co można wykorzystać, nakład zmian w pipeline/architekturze, ograniczenia).
     3. **Key Takeaways** (punktowana lista detali technicznych, modeli, datasetów i konkretnych wyników liczbowych).
     4. **Linki i źródła** (podany URL, ewentualne repozytorium z tekstu oraz lista autorów).