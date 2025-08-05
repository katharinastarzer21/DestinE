import yaml
import os

root = "production"
main_sections = ["HDA", "HOOK", "STACK"]

toc = [{"file": "index.md"}]  

tag_gallery_dir = "galleries_by_tag"
if os.path.exists(tag_gallery_dir):
    files = sorted(os.listdir(tag_gallery_dir))
    print(f"📁 {tag_gallery_dir} enthält {len(files)} Datei(en)")
    for fname in files:
        print("🔹", fname)
        if fname.endswith(".md"):
            toc.append({
                "file": f"{tag_gallery_dir}/{fname}",
                "hidden": True
            })
else:
    print("⚠️  Ordner galleries_by_tag/ nicht gefunden!")

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

with open("myst.yml", "w", encoding="utf-8") as f:
    yaml.dump(config, f, sort_keys=False)

print("✅ myst.yml erfolgreich erstellt.")
