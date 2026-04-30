# Run the dashboard and HTML report

## Setup

```bash
pip install -r requirements.txt
```

## Tests + themed report

`pytest.ini` writes **`ui/report.html`** with **`assets/style.css`**.

```bash
pytest
```

## Flask

From the project root (this folder):

```bash
pytest
set FLASK_DEBUG=1
python app.py
```

(On PowerShell: `$env:FLASK_DEBUG = "1"` before `python app.py` for auto-reload.)

- Dashboard: http://127.0.0.1:5000/
- Report: http://127.0.0.1:5000/report.html

## VS Code Live Server

Open the project root in Live Server, then:

- http://127.0.0.1:5500/ui/index.html
- http://127.0.0.1:5500/ui/report.html (after `pytest`)

## Windows

```bat
run_ui_demo.bat
```

Installs dependencies, runs tests, opens `ui\index.html` and `ui\report.html`.
