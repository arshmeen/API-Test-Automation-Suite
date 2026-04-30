# Run UI + Report (Go Live)

## One-time setup

```bash
pip install -r requirements.txt
```

## Generate themed report

`pytest.ini` is preconfigured, so just run:

```bash
pytest
```

This creates `ui/report.html` automatically.

## Open with Live Server

Start Go Live from the `api-test-suite` folder, then open:

- `http://127.0.0.1:5500/ui/index.html`
- `http://127.0.0.1:5500/ui/report.html`

## Windows shortcut

Run:

```bat
run_ui_demo.bat
```

It installs deps, runs tests, and opens both pages.

## Flask (same folder as `app.py`)

From `api-test-suite`:

```bash
pip install -r requirements.txt
pytest
python app.py
```

Open **http://127.0.0.1:5000/** and **http://127.0.0.1:5000/report.html**.

**Note:** If you also have a folder named `api test` on your machine, that is a separate copy. Run commands from **one** project folder only—the one that contains `app.py`.
