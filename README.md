# Academic Portfolio Site

A one-page Flask site for a Digital Humanities academic portfolio: hero,
about, a projects catalog, and a "colophon" of social links (Substack,
YouTube, LinkedIn, Bluesky).

## Run it (recommended way — VS Code terminal)

```bash
cd dh_portfolio
pip install -r requirements.txt
python app.py
```

Then open the link printed in the terminal, usually **http://127.0.0.1:5000**.

Leave `debug=True` in `app.py` while you're editing — the page auto-reloads
on save.

## Run it from a Jupyter notebook cell

Open `run_in_notebook.ipynb` in VS Code and run its cells in order. It starts
the same Flask app in a background thread so the notebook doesn't hang.

## Edit your content

Open `app.py` and edit the `SITE` dictionary near the top:

- `name`, `role`, `tagline`, `institution`, `email`
- `about` — your bio paragraph
- `projects` — a list of dicts, one per project (`title`, `year`, `type`,
  `tools`, `description`, `link`). Add or remove entries freely.
- `social` — your Substack / YouTube / LinkedIn / Bluesky URLs. Set any
  field to `""` to hide that link.

Save the file and refresh the browser — no other files need editing for
basic content changes.

## Project structure

```
dh_portfolio/
├── app.py                  # Flask app + your content (SITE dict)
├── requirements.txt
├── run_in_notebook.ipynb    # optional Jupyter launcher
├── templates/
│   ├── index.html          # page markup
│   └── icons/               # small SVG icons for each platform
└── static/
    ├── style.css            # all design/styling
    └── script.js            # footer year + scroll-in animation
```

## Deploying it live

Once you're happy with it, free/cheap hosts that work well with Flask:
**Render, Railway, PythonAnywhere, or Fly.io.** They typically just need
this folder plus a start command like `gunicorn app:app`.

## Design notes

The visual motif borrows from TEI/XML markup — the encoding language DH
scholars use to structure texts — as small tag-style labels (`<abstract>`,
`type="..."`, `rel="substack"`) throughout the page. Palette is deep ink
navy with parchment text, a muted gold for links/accents, and a brick-rust
for the markup tags. Fonts: Fraunces (display), Source Serif 4 (body),
IBM Plex Mono (the tag labels).
