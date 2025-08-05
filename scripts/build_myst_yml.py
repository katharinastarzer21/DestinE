import yaml
import os

root = "production"
main_sections = ["HDA", "HOOK", "STACK"]

toc = [{"file": "index.md"}]  

for section in main_sections:
    entry = {
        "title": section,
        "file": f"galleries/{section}.md",  
        "children": []
    }

    section_path = os.path.join(root, section)
    for dirpath, _, filenames in os.walk(section_path):
        for f in sorted(filenames):
            if f.endswith(".ipynb"):
                full_path = os.path.join(dirpath, f)
                rel_path = os.path.relpath(full_path, ".").replace("\\", "/")
                entry["children"].append({"file": rel_path})

    toc.append(entry)

tag_gallery_dir = "galleries_by_tag"
if os.path.exists(tag_gallery_dir):
    for fname in sorted(os.listdir(tag_gallery_dir)):
        if fname.endswith(".md"):
            toc.append({"includehidden:": f"{tag_gallery_dir}/{fname}"})


config = {
    "version": 1,
    "project": {
        "title": "DEDL Notebook Gallery",
        "toc": toc
    },
    "site": {
        "template": "book-theme",
        "options": {
            "style": "_static/custom.css",
            "favicon": "img/EUMETSAT-icon.ico",
            "logo": "img/logo_bar.png",
            "hide_footer_links": True,
        },
        "parts": {
            "footer": "footer.md"
        }
    }
}

# === Schreiben in myst.yml ===
with open("myst.yml", "w", encoding="utf-8") as f:
    yaml.dump(config, f, sort_keys=False)

print("✅ myst.yml erfolgreich erstellt mit gallery.md-Einträgen.")
