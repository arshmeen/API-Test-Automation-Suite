"""
Local web server for the themed dashboard and pytest HTML report.

Run from this directory:
    python app.py

Then open http://127.0.0.1:5000/
"""
from __future__ import annotations

import os

from flask import Flask, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_DIR = os.path.join(BASE_DIR, "ui")

app = Flask(__name__, static_folder=UI_DIR, static_url_path="")


def _no_cache(resp):
    """Avoid stale report.html after re-running pytest."""
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    resp.headers["Pragma"] = "no-cache"
    return resp


@app.route("/")
def index():
    return _no_cache(send_from_directory(UI_DIR, "index.html"))


@app.route("/report.html")
def report():
    ui_report = os.path.join(UI_DIR, "report.html")
    root_report = os.path.join(BASE_DIR, "report.html")
    if os.path.isfile(ui_report):
        return _no_cache(send_from_directory(UI_DIR, "report.html"))
    if os.path.isfile(root_report):
        return _no_cache(send_from_directory(BASE_DIR, "report.html"))
    return (
        "No report yet. Run: python -m pytest",
        404,
        {"Content-Type": "text/plain; charset=utf-8"},
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    # Set FLASK_DEBUG=1 locally for the reloader; omit on production (e.g. Render).
    debug = os.environ.get("FLASK_DEBUG") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
