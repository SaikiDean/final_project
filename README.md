# Maturitní projekt - webová stránka zabývající se recepty
## Popis projektu
- cílem projektu je vytvořit fungující webovou stránku,
kde bude funkční registrace a přihlášení uživatele
- uživatel bude moci napsat své vlastní recepty, které se samozřejmě uloží do databáze a zobrazí se na stránce tam, 
kde mají a případně si bude moct uživatel připnout recept do oblíbených
- recepty budou roztříděny dle kategorií (např.: oběd, snídaně, atd..)


## Použité technologie
- Projekt je vytvořen v Djangu
- Databáze využívá SQlite3
- Templates = šablony jsou napsány v HTML

## Cíle
(jestliže se vyskytuje u některého z cílů křížek, stále se na daném cíli pracuje)
- data (recepty) se ukládají do databáze ✔
- třídění receptů dle kategorie ✔
- funkční login a registrace ✔
- správné zobrazování obrázků ×
- profil uživatele a přidávání si receptů do oblíbených × 
- slušný design ×

## Spuštění projektu pro Windows:
```
git clone https://github.com/SaikiDean/final_project
cd final_project
python -m venv myvenv
myvenv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

## Spuštění projektu pro Linux
```
git clone https://github.com/SaikiDean/final_project
cd final_project
virtualenv -p python myvenv
source myvenv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```