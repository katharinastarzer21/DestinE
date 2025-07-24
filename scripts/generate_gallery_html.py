import os
import nbformat
import yaml
from pathlib import Path
from collections import defaultdict

ROOT_DIR = Path("notebooks")

def extract_metadata_from_notebook(nb_path):
    try:
        nb = nbformat.read(nb_path, as_version=4)
        first_cell = nb.cells[0]
        if first_cell.cell_type == "markdown" and first_cell.source.strip().startswith("---"):
            parts = first_cell.source.strip().split('---')
            if len(parts) >= 3:
                yaml_content = parts[1]
                metadata = yaml.safe_load(yaml_content)
                metadata["file"] = str(nb_path).replace("\\", "/").replace(".ipynb", ".html")
                return metadata
    except Exception as e:
        print(f"[WARN] Failed to read {nb_path}: {e}")
    return None

def build_html(metadata_list):
    all_tags = sorted({tag for md in metadata_list for tag in md.get("tags", [])})

    # HTML Head + Styles + FilterBar
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Notebook Gallery</title>
  <style>
    body {
      font-family: sans-serif;
      padding: 2em;
      background-color: #f4f8fc;
    }
    .filter-bar {
      margin-bottom: 2em;
    }
    .filter-bar button {
      background: #e0ecf7;
      border: none;
      padding: 6px 12px;
      margin: 4px;
      border-radius: 6px;
      cursor: pointer;
    }
    .filter-bar button:hover {
      background: #c5dff3;
    }
    .card {
      display: flex;
      align-items: center;
      background: white;
      border-radius: 6px;
      border: 1px solid #cddff1;
      box-shadow: 1px 1px 4px #dfeaf5;
      padding: 16px;
      margin-bottom: 20px;
    }
    .card img {
      width: 100px;
      height: 80px;
      object-fit: contain;
      margin-right: 24px;
    }
    .card h3 {
      margin: 0 0 6px 0;
    }
    .card p {
      margin: 0 0 6px 0;
    }
    .card .tags span {
      background: #e6f0fa;
      padding: 2px 10px;
      border-radius: 10px;
      margin-right: 5px;
      font-size: 0.8em;
    }
  </style>
</head>
<body>

<div class="filter-bar">
  <button onclick="filterCards('all')">All</button>"""

    for tag in all_tags:
        html += f'<button onclick="filterCards(\'{tag}\')">{tag}</button>'
    html += "</div>\n"

    # Notebook Cards
    html += '<div class="gallery">\n'
    for md in metadata_list:
        tags = md.get("tags", [])
        tag_str = ",".join(tags)
        html += f"""
  <div class="card" data-tags="{tag_str}">
    <img src="{md.get('thumbnail', 'img/thumbs/default.png')}" alt="thumbnail">
    <div>
      <h3><a href="{md['file']}">{md.get('title', 'Untitled')}</a></h3>
      <p>{md.get('description', '')}</p>
      <div class="tags">{" ".join(f"<span>{t}</span>" for t in tags)}</div>
    </div>
  </div>
"""
    html += "</div>\n"

    # JS Filtering
    html += """
<script>
function filterCards(tag) {
  document.querySelectorAll('.card').forEach(card => {
    const tags = card.dataset.tags;
    if (tag === 'all' || tags.includes(tag)) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });
}
</script>
</body>
</html>"""
    return html

def main():
    metadata_list = []
    for nb_path in ROOT_DIR.rglob("*.ipynb"):
        md = extract_metadata_from_notebook(nb_path)
        if md:
            metadata_list.append(md)

    html = build_html(metadata_list)
    print(html)

if __name__ == "__main__":
    main()
