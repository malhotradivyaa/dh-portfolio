"""
Academic Digital Humanities Portfolio
--------------------------------------
A small Flask site: one page, edited from the data below.

HOW TO RUN (recommended — VS Code terminal, not a notebook cell):
    1. Open this folder in VS Code.
    2. Open a terminal (Terminal > New Terminal).
    3. pip install -r requirements.txt
    4. python app.py
    5. Open the printed link (http://127.0.0.1:5000) in your browser.

HOW TO RUN FROM A JUPYTER NOTEBOOK CELL (if you specifically want that):
    See run_in_notebook.ipynb in this folder — it starts the same app
    in a background thread so the cell doesn't block forever.

EDIT YOUR CONTENT:
    Everything you need to personalize — your name, bio, projects,
    and social links — is in the SITE dictionary just below. You do
    not need to touch the HTML/CSS to update your content.
"""

from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------------
# 1. EDIT THIS SECTION WITH YOUR OWN INFORMATION
# ---------------------------------------------------------------------------

SITE = {
    "name": "Your Name",
    "role": "Digital Humanities Scholar",
    "tagline": "Reading texts at scale — corpora, code, and cultural history.",
    "institution": "Department of English, Your University",
    "email": "you@university.edu",

    "about": (
        "I work at the intersection of literary history and computational "
        "methods, building tools and arguments that treat texts as both "
        "objects of close reading and structured data. My projects combine "
        "corpus analysis, network visualization, and archival research to "
        "ask questions that neither pure humanities nor pure computation "
        "could answer alone."
    ),

    # One entry per project. "tags" show up as small markup-style labels
    # (an homage to TEI/XML encoding, which is core to DH work).
    "projects": [
        {
            "title": "Mapping the Correspondence Network of the Bloomsbury Group",
            "year": "2025",
            "type": "network analysis",
            "tools": "Python, NetworkX, Gephi",
            "description": (
                "A relational map of over 3,000 letters exchanged between "
                "1905 and 1941, revealing shifting clusters of intellectual "
                "influence within the group."
            ),
            "link": "#",
        },
        {
            "title": "TEI Encoding of the Regional Almanac Collection",
            "year": "2024",
            "type": "text encoding / archive",
            "tools": "TEI/XML, oXygen, Python",
            "description": (
                "A structured, searchable edition of 40 nineteenth-century "
                "almanacs, encoded to support queries across authorship, "
                "genre, and marginal annotation."
            ),
            "link": "#",
        },
        {
            "title": "Sentiment Drift in Serialized Victorian Fiction",
            "year": "2023",
            "type": "computational text analysis",
            "tools": "Python, spaCy, pandas",
            "description": (
                "A chapter-by-chapter sentiment model applied across twelve "
                "serialized novels, tracing how publication schedules shaped "
                "emotional pacing."
            ),
            "link": "#",
        },
    ],

    # Update the URLs to your own accounts. Leave a field as "" to hide it.
    "social": {
        "substack": "https://yourname.substack.com",
        "youtube": "https://youtube.com/@yourname",
        "linkedin": "https://linkedin.com/in/yourname",
        "bluesky": "https://bsky.app/profile/yourname.bsky.social",
    },
}

# ---------------------------------------------------------------------------
# 2. ROUTES — you shouldn't need to touch this section
# ---------------------------------------------------------------------------


@app.route("/")
def home():
    return render_template("index.html", site=SITE)


if __name__ == "__main__":
    app.run(debug=True)
