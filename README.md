# Karan Tanwar — Simple Flask Portfolio (Flask)

This small Flask application serves a Bootstrap-styled personal/portfolio page at the root route (`/`). The page content (in `templates/index.html`) currently introduces "Karan Tanwar" and lists experience, skills and badges.

## Dependencies

The project requires Python 3.8+ and Flask. The pinned requirement in this repo is:

```
Flask>=2.0
```

## Quick start (Windows PowerShell)

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
python app.py
```

4. Open the app in your browser:

```
http://127.0.0.1:5000
```

## Files of interest

- `app.py` — Flask application. It defines a single route `/` that renders `templates/index.html`.
- `templates/index.html` — The Bootstrap-styled HTML template that displays the greeting and portfolio information.
- `requirements.txt` — Python dependencies.

## Quick verification (optional)

You can quickly check the app route using Flask's test client from the repo root (this does not start the server):

```powershell
python - <<'PY'
from app import app

with app.test_client() as c:
    r = c.get('/')
    print('status:', r.status_code)
    print('contains "Karan"?', 'Karan' in r.get_data(as_text=True))
PY
```

## Notes

- The template currently uses the Bootstrap CDN and inline styles for a simple polished look.
- If you want the page to say exactly "Hello Karan" instead of the current portfolio content, edit `templates/index.html` (replace or add a prominent heading).

If you'd like, I can (a) change the template to display a headline that says exactly "Hello Karan" in a specific style, or (b) add a small unit test that asserts the greeting text. Tell me which you prefer and I'll update the files.
# Simple Flask App — Hello Karan

This is a tiny Flask app that renders a friendly "Hello Karan" page.

Quick start (Windows PowerShell):

```powershell
# Create and activate a venv (optional but recommended)
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Then open http://127.0.0.1:5000 in your browser
```

Files added:
- `app.py` — Flask application
- `templates/index.html` — HTML template that shows "Hello Karan"
- `requirements.txt` — required Python packages
