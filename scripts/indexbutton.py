import os

index_path = "index.md"
tag_gallery_dir = "galleries_by_tag"
start_marker = "### Filter Notebooks by Tags"
button_prefix = "{button}`"
button_suffix = "`"


tag_files = sorted([
    f for f in os.listdir(tag_gallery_dir)
    if f.endswith(".md") and f.startswith("tag-")
])

with open(index_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

existing_buttons = set()
for line in lines:
    if line.strip().startswith(button_prefix):
        content = line.strip()[len(button_prefix):-len(button_suffix)]
        if "<" in content and ">" in content:
            target = content.split("<")[1].split(">")[0].strip()
            existing_buttons.add(target)


new_buttons = []
for fname in tag_files:
    path = f"{tag_gallery_dir}/{fname}"
    if path not in existing_buttons:
        tag = fname.replace("tag-", "").replace(".md", "").replace("-", " ").title()
        new_buttons.append(f"{button_prefix}{tag} <{path}>{button_suffix}\n")

if new_buttons:
    new_lines = []
    inside_filter_section = False
    for line in lines:
        new_lines.append(line)
        if line.strip().startswith(start_marker):
            inside_filter_section = True
    if inside_filter_section:
        new_lines.append("\n")
        new_lines.extend(new_buttons)

    with open(index_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"{len(new_buttons)} new buttons added.")
else:
    print("No new Keywords")
