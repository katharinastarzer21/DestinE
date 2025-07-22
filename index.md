---
title: Interaktive Galerie
html:
  toc: false
---

# 🧪 Interaktive Galerie mit Tag-Filter

```{raw} html
<div id="tag-filter-buttons"></div>
<div id="gallery-container"></div>
<script>const galleryData = [{"title": "Sentinel Viewer", "file": "notebooks/sentinel.ipynb", "tags": ["satellite", "viewer"], "description": "Datenanalyse mit PySTAC"}, {"title": "Climate Analysis", "file": "notebooks/climate.ipynb", "tags": ["climate", "temperature"], "description": "ERA5-Auswertung"}];</script>

<script>
function buildGallery(data) {
  const container = document.getElementById("gallery-container");
  const filter = document.getElementById("tag-filter-buttons");
  const allTags = new Set(data.flatMap(e => e.tags));
  const show = tag => {
    document.querySelectorAll(".gallery-card").forEach(card => {
      const tags = card.dataset.tags.split(",");
      card.style.display = tag === "" || tags.includes(tag) ? "" : "none";
    });
  };
  const addBtn = (txt, fn) => {
    const btn = document.createElement("button");
    btn.textContent = txt;
    btn.onclick = fn;
    filter.appendChild(btn);
  };
  addBtn("Alle", () => show(""));
  [...allTags].sort().forEach(tag => addBtn(tag, () => show(tag)));
  data.forEach(e => {
    const card = document.createElement("div");
    card.className = "gallery-card";
    card.dataset.tags = e.tags.join(",");
    const link = e.file.replace(".ipynb", ".html");
    card.innerHTML = `<h3><a href="${link}">${e.title}</a></h3>
                      <p>${e.description}</p>
                      <small>Tags: ${e.tags.join(", ")}</small>`;
    container.appendChild(card);
  });
  show("");
}
document.addEventListener("DOMContentLoaded", () => buildGallery(galleryData));
</script>
<style>
  #tag-filter-buttons button {
    margin: 0.3em;
    padding: 0.4em 0.8em;
    border-radius: 6px;
    border: 1px solid #aaa;
    background-color: #eee;
    cursor: pointer;
  }
  .gallery-card {
    border: 1px solid #ccc;
    padding: 1em;
    border-radius: 10px;
    margin: 1em 0;
    background-color: #f9f9f9;
  }
</style>

```
