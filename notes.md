### uv venv
```bash
uv init --app --python 3.13
uv add flask
uv add --dev ruff
source .venv/bin/activate
deactivate
uv sync --upgrade
```

### vscode exts
- flask
- jinja


### start server
```bash
FLASK_APP=mblog.py flask run
```

