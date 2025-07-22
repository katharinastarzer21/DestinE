import yaml
from pathlib import Path

with open("myst.yml", "r") as f:
    config = yaml.safe_load(f)

entries = []

def extract_entries(children, parent=None):
    for item in children:
        if isinstance(item, dict):
            file = item.get("file")
            tags = item.get("tags", [])
            title = item.get("title", Path(file).stem if file else None)
            if file and file.endswith(".ipynb"):
                entries.append({
                    "title": title,
                    "file": file,
                    "tags": tags,
                    "parent": parent
                })
            elif "children" in item:
                extract_entries(item["children"], parent=item.get("title", parent))

toc = config.get("project", {}).get("toc", [])
extract_entries(toc)

html = ['<div id="tag-filter-buttons" style="margin-bottom: 1rem;"></div>']
html.append('<div id="gallery-container" class="gallery"></div>')
html.append("<script>const galleryData = " + str(entries).replace("'", '"') + ";</script>")
html.append("""
<script>
function buildGallery(data) {
  const container = document.getElementById("gallery-container");
  const filterContainer = document.getElementById("tag-filter-buttons");
  const allTags = new Set();
  data.forEach(entry => entry.tags.forEach(tag => allTags.add(tag)));

  const allButton = document.createElement("button");
  allButton.textContent = "Alle";
  allButton.onclick = () => updateGallery("");
  filterContainer.appendChild(allButton);

  Array.from(allTags).sort().forEach(tag => {
    const btn = document.createElement("button");
    btn.textContent = tag;
    btn.onclick = () => updateGallery(tag);
    filterContainer.appendChild(btn);
  });

  data.forEach(entry => {
    const card = document.createElement("div");
    card.className = "gallery-card";
    card.setAttribute("data-tags", entry.tags.join(","));
    const link = entry.file.replace(".ipynb", ".html");
    card.innerHTML = `<h3><a href="${link}">${entry.title}</a></h3>
      <p><strong>Pfad:</strong> ${entry.file}</p>
      <p><strong>Tags:</strong> ${entry.tags.join(", ")}</p>`;
    container.appendChild(card);
  });

  function updateGallery(tag) {
    document.querySelectorAll(".gallery-card").forEach(card => {
      const tags = card.getAttribute("data-tags").split(",");
      card.style.display = tag === "" || tags.includes(tag) ? "block" : "none";
    });
  }

  updateGallery("");
}
document.addEventListener("DOMContentLoaded", () => buildGallery(galleryData));
</script>

<style>
#tag-filter-buttons button {
  margin: 0.3em;
  padding: 0.4em 0.8em;
  border-radius: 6px;
  border: 1px solid #aaa;
  background: #f1f1f1;
  cursor: pointer;
}
.gallery-card {
  border: 1px solid #ddd;
  padding: 1em;
  border-radius: 8px;
  margin-bottom: 1em;
  background: #fcfcfc;
}
</style>
""")
Path("gallery_fragment.html").write_text("\n".join(html))