#!/usr/bin/env python3
"""
gdd_to_pdf.py — Export docs/human-gdd.md to docs/human-gdd.pdf

Requires:
  pip install -r requirements.txt          (markdown, weasyprint)
  npm install -g @mermaid-js/mermaid-cli   (mmdc, for diagram rendering)

Run from the project root:
  python3 workflow/scripts/gdd_to_pdf.py
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

INPUT_FILE = Path("docs/human-gdd.md")
OUTPUT_FILE = Path("docs/human-gdd.pdf")

CSS = """
body {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #222;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}
h1 {
    font-size: 2em;
    border-bottom: 2px solid #333;
    padding-bottom: 0.3em;
    page-break-before: always;
}
h1:first-of-type { page-break-before: avoid; }
h2 {
    font-size: 1.5em;
    border-bottom: 1px solid #ccc;
    padding-bottom: 0.2em;
    page-break-before: always;
}
h3 { font-size: 1.2em; }
h4 { font-size: 1em; }
code {
    font-family: 'Courier New', monospace;
    background: #f4f4f4;
    padding: 2px 4px;
    border-radius: 3px;
    font-size: 0.9em;
}
pre {
    background: #f4f4f4;
    border: 1px solid #ddd;
    padding: 12px;
    border-radius: 4px;
    overflow-x: auto;
}
pre code { background: none; padding: 0; }
blockquote {
    border-left: 3px solid #aaa;
    margin: 0;
    padding-left: 1em;
    color: #555;
}
img { max-width: 100%; height: auto; display: block; margin: 1em auto; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: left; }
th { background: #f0f0f0; font-weight: bold; }
tr:nth-child(even) { background: #fafafa; }
ul, ol { padding-left: 1.5em; }
hr { border: none; border-top: 1px solid #ddd; margin: 2em 0; }
"""


# ---------------------------------------------------------------------------
# Dependency checks
# ---------------------------------------------------------------------------

def check_python_packages() -> None:
    missing = []
    try:
        import markdown  # noqa: F401
    except ImportError:
        missing.append("markdown")
    try:
        import weasyprint  # noqa: F401
    except ImportError:
        missing.append("weasyprint")
    if missing:
        print(f"ERROR: Missing Python packages: {', '.join(missing)}")
        print("       Install with: pip install -r requirements.txt")
        sys.exit(1)


def check_mmdc() -> None:
    if shutil.which("mmdc") is None:
        print("ERROR: mermaid-cli (mmdc) not found on PATH.")
        print("       Install with: npm install -g @mermaid-js/mermaid-cli")
        sys.exit(1)


# ---------------------------------------------------------------------------
# Mermaid rendering
# ---------------------------------------------------------------------------

_MERMAID_PATTERN = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)


def render_mermaid_blocks(md_text: str, tmp_dir: str) -> str:
    """
    Replace each ```mermaid ... ``` block with a rendered PNG image reference.
    Uses mmdc (mermaid-cli) for fully offline rendering.
    Falls back to a plain code block with a warning if rendering fails.
    """
    diagram_index = [0]

    def replace_block(match: re.Match) -> str:
        source = match.group(1)
        idx = diagram_index[0]
        diagram_index[0] += 1

        mmd_path = Path(tmp_dir) / f"diagram_{idx}.mmd"
        png_path = Path(tmp_dir) / f"diagram_{idx}.png"

        mmd_path.write_text(source, encoding="utf-8")

        result = subprocess.run(
            ["mmdc", "-i", str(mmd_path), "-o", str(png_path),
             "-b", "white", "--width", "900"],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0 or not png_path.exists():
            print(f"  WARNING: Could not render diagram {idx}: {result.stderr.strip()}")
            return f"```\n{source}```"

        print(f"  Rendered diagram {idx} → {png_path.name}")
        # Absolute path so weasyprint resolves the file regardless of cwd
        return f"![diagram]({png_path.resolve().as_posix()})"

    return _MERMAID_PATTERN.sub(replace_block, md_text)


# ---------------------------------------------------------------------------
# HTML conversion
# ---------------------------------------------------------------------------

def build_html(md_text: str) -> str:
    """Convert markdown to a full HTML document with embedded CSS."""
    import markdown as md_lib

    extensions = ["tables", "fenced_code", "toc", "nl2br", "extra"]
    body = md_lib.markdown(md_text, extensions=extensions)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
{CSS}
</style>
</head>
<body>
{body}
</body>
</html>"""


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if not INPUT_FILE.exists():
        print(f"ERROR: {INPUT_FILE} not found.")
        print("       Complete gdd-1 through gdd-6 before exporting.")
        sys.exit(1)

    check_python_packages()
    check_mmdc()

    print(f"Reading {INPUT_FILE} ...")
    md_text = INPUT_FILE.read_text(encoding="utf-8")

    tmp_dir = tempfile.mkdtemp(prefix="gdd_pdf_")
    try:
        print("Rendering Mermaid diagrams ...")
        md_text = render_mermaid_blocks(md_text, tmp_dir)

        print("Converting to HTML ...")
        html = build_html(md_text)

        print(f"Exporting PDF → {OUTPUT_FILE} ...")
        import weasyprint
        weasyprint.HTML(
            string=html,
            base_url=str(Path.cwd()),
        ).write_pdf(str(OUTPUT_FILE))

        print(f"\nDone: {OUTPUT_FILE.resolve()}")
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
