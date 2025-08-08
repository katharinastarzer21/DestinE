import os

index_path = "index.md"
tag_gallery_dir = "galleries_by_tag"
start_marker = "### Filter Notebooks by Tags"
button_prefix = "{button}`"
button_suffix = "`"

tag_files = sorted(
    f for f in os.listdir(tag_gallery_dir)
    if f.endswith(".md") and f.startswith("tag-")
)

with open(index_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

existing_targets = set()
for line in lines:
    s = line.strip()
    if s.startswith(button_prefix) and s.endswith(button_suffix) and "<" in s and ">" in s:
        target = s.split("<", 1)[1].split(">", 1)[0].strip()
        existing_targets.add(target)

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

try:
    marker_idx = next(i for i, ln in enumerate(lines) if ln.strip() == start_marker)
except StopIteration:
    print(f"Marker '{start_marker}' not found in {index_path}. No changes made.")
    raise SystemExit(0)

insert_idx = marker_idx + 1
block = []

if insert_idx >= len(lines) or lines[insert_idx].strip() != "":
    block.append("\n")  

block.extend(new_buttons)
block.append("\n")  

new_lines = lines[:insert_idx] + block + lines[insert_idx:]

with open(index_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"{len(new_buttons)} new buttons added at the top of the filter section.")
