import os

index_path = "index.md"
tag_gallery_dir = "galleries_by_tag"
start_marker = "### Filter Notebooks by Tags"
button_prefix = "{button}`"
button_suffix = "`"

if not os.path.isdir(tag_gallery_dir):
    print(f"Directory not found: {tag_gallery_dir}. No changes made.")
    raise SystemExit(0)

tag_files = sorted(
    f for f in os.listdir(tag_gallery_dir)
    if f.startswith("tag-") and f.endswith(".md")
)

new_buttons = []
for fname in tag_files:
    path = f"{tag_gallery_dir}/{fname}"
    tag_label = (
        fname.replace("tag-", "")
             .replace(".md", "")
             .replace("-", " ")
             .title()
    )
    new_buttons.append(f"{button_prefix}{tag_label} <{path}>{button_suffix}\n")

with open(index_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

try:
    marker_idx = next(i for i, ln in enumerate(lines) if ln.strip() == start_marker)
except StopIteration:
    print(f"Marker '{start_marker}' not found in {index_path}.")
    raise SystemExit(1)

start_idx = marker_idx + 1

if start_idx < len(lines) and lines[start_idx].strip() == "":
    start_idx += 1

end_idx = start_idx
while end_idx < len(lines):
    s = lines[end_idx].strip()
    if not s:
        end_idx += 1
        continue
    if s.startswith(button_prefix) and s.endswith(button_suffix):
        end_idx += 1
        continue
    break

replacement = []
replacement.append("\n")
replacement.extend(new_buttons)
replacement.append("\n")

new_lines = lines[:start_idx] + replacement + lines[end_idx:]

with open(index_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"✅ Replaced button block with {len(new_buttons)} buttons (alphabetical).")
