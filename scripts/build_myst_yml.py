import yaml
import os

root = "production"
main_sections = ["HDA", "HOOK", "STACK"]
toc = [{"file": "index.md"}]

for section in main_sections:
    section_path = os.path.join(root, section)
    entry = {"title": section, "file": f"{section_path}/gallery.md", "children": []}
    for dirpath, _, filenames in os.walk(section_path):
        for f in sorted(filenames):
            if f.endswith(".ipynb"):
                full_path = os.path.join(dirpath, f)
                relative_path = os.path.normpath(full_path)
                entry["children"].append({"file": relative_path})
    toc.append(entry)

config = {
    "version": 1,
    "project": {
        "title": "DEDL Notebook Gallery",
        "toc": toc
    },
    "site": {
        "template": "book-theme",
        "hide_footer_links": True,
        "options": {
            "style": "_static/custom.css",
            "favicon": "img/EUMETSAT-icon.ico",
            "logo": "img/logo_bar.png"
        },
        "parts": {
            "footer": "footer.md"
        }
    }
}

with open("myst.yml", "w") as f:
    yaml.dump(config, f, sort_keys=False)

print("✅ myst.yml updated.")
