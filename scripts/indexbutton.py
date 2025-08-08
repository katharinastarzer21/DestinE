import os

index_path = "index.md"
tag_gallery_dir = "galleries_by_tag"
start_marker = "### Filter Notebooks by Tags"
button_prefix = "{button}`"
button_suffix = "`"

# Alle Tag-Dateien holen
tag_files = sorted(
    f for f in os.listdir(tag_gallery_dir)
    if f.endswith(".md") and f.startswith("tag-")
)

# index.md lesen
with open(index_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Existierende Button-Ziele sammeln (damit wir keine Duplikate erzeugen)
existing_targets = set()
for line in lines:
    s = line.strip()
    if s.startswith(button_prefix) and s.endswith(button_suffix) and "<" in s and ">" in s:
        target = s.split("<", 1)[1].split(">", 1)[0].strip()
        existing_targets.add(target)

# Neue Buttons vorbereiten (nur für noch nicht vorhandene Tag-Seiten)
new_buttons = []
for fname in tag_files:
    path = f"{tag_gallery_dir}/{fname}"
    if path not in existing_targets:
        tag_label = (
            fname.replace("tag-", "")
                 .replace(".md", "")
                 .replace("-", " ")
                 .title()
        )
        new_buttons.append(f"{button_prefix}{tag_label} <{path}>{button_suffix}\n")

if not new_buttons:
    print("No new Keywords")
    raise SystemExit(0)

# Einfügeposition: direkt NACH der Marker-Zeile
try:
    marker_idx = next(i for i, ln in enumerate(lines) if ln.strip() == start_marker)
except StopIteration:
    print(f"Marker '{start_marker}' not found in {index_path}. No changes made.")
    raise SystemExit(0)

# Falls direkt nach dem Marker eine Leerzeile kommt, Buttons danach einfügen;
# ansonsten fügen wir noch eine Leerzeile ein, um Luft zu schaffen.
insert_idx = marker_idx + 1
block = []

if insert_idx >= len(lines) or lines[insert_idx].strip() != "":
    block.append("\n")  # eine Leerzeile unter der Überschrift

# Neue Buttons OBEN im Abschnitt einfügen
block.extend(new_buttons)
block.append("\n")  # nach den neuen Buttons noch eine Leerzeile

# Neues Dokument zusammenbauen: bis insert_idx, Block, dann Rest
new_lines = lines[:insert_idx] + block + lines[insert_idx:]

with open(index_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"{len(new_buttons)} new buttons added at the top of the filter section.")
