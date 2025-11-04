
# Flask CRUD Lab — Complete Solution

A minimal Flask app that demonstrates Create, Read, Update, Delete (CRUD) using SQLite and SQLAlchemy.
It follows the structure from your lab handout.

## Quickstart

1) Create & activate a virtual environment (Windows PowerShell):
```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```
macOS / Linux:
```bash
python3 -m venv env
source env/bin/activate
```

2) Install dependencies:
```bash
pip install -r requirements.txt
```

3) Run the app:
```bash
python app.py
```
Visit http://127.0.0.1:5000/ in your browser.

## Notes
- The database file `firstapp.db` is created automatically on first run (in the project root).
- Use the form on the homepage to add students; table shows all records; buttons let you update/delete.
- Change `SECRET_KEY` in `app.py` for production.
