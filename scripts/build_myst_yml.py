import yaml
import os

if os.path.exists("myst.yml"):
    os.remove("myst.yml")

PRODUCTION_ROOT = "production"
main_sections = [d for d in os.listdir(PRODUCTION_ROOT) if os.path.isdir(os.path.join(PRODUCTION_ROOT, d))]

# ✔ Korrekt geschriebener Index-Eintrag mit hide_sidebar + children

toc = [
    {"file": "index.md"},
    {"title": "contribute", 
     "file": "contribute.md"},
]

# ✔ Erzeuge TOC-Einträge für jede Hauptsektion (STACK, HDA, HOOK, ...)
for section in main_sections:
    entry = {
        "title": section,
        "file": f"galleries/{section}.md",
        "children": []
    }

    section_path = os.path.join(PRODUCTION_ROOT , section)
    for dirpath, _, filenames in os.walk(section_path):
        for f in sorted(filenames):
            if f.endswith(".ipynb"):
                full_path = os.path.join(dirpath, f)
                rel_path = os.path.relpath(full_path, ".").replace("\\", "/")
                entry["children"].append({"file": rel_path})

    toc.append(entry)

# ✔ Füge alle Tag-Seiten als separate TOC-Einträge hinzu
tag_gallery_dir = "galleries_by_tag"
if os.path.exists(tag_gallery_dir):
    for fname in sorted(os.listdir(tag_gallery_dir)):
        if fname.endswith(".md"):
            toc.append({
                "file": f"{tag_gallery_dir}/{fname}",
            })

# ✔ Konfigurationsblock mit book-theme, Logo, CSS etc.
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
            "hide_outline": True
        },
        "parts": {
            "footer": "footer.md"
        }
    }
}

# ✔ Speichere myst.yml
with open("myst.yml", "w", encoding="utf-8") as f:
    yaml.dump(config, f, sort_keys=False)

print("✅ myst.yml erfolgreich erstellt mit index, hide_sidebar und contribute.md.")
