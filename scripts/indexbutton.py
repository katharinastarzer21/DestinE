import os

index_path = "index.md"
tag_gallery_dir = "galleries_by_tag"
start_marker = "## Notebook Filter"
button_prefix = "{button}`"
button_suffix = "`"


tag_files = sorted([
    f for f in os.listdir(tag_gallery_dir)
    if f.endswith(".md") and f.startswith("tag-")
])


buttons = []
for fname in tag_files:
    tag = fname.replace("tag-", "").replace(".md", "").replace("-", " ").title()
    buttons.append(f"{button_prefix}{tag} <{tag_gallery_dir}/{fname}>{button_suffix}")


with open(index_path, "r", encoding="utf-8") as f:
    lines = f.readlines()


new_lines = []
inside_button_section = False
for line in lines:
    if line.strip().startswith(start_marker):
        new_lines.append(line)
        inside_button_section = True
        continue

    if inside_button_section:
        if not line.strip().startswith("{button}`"):
            inside_button_section = False
            new_lines.append("\n")
        else:
            continue

    if not inside_button_section:
        new_lines.append(line)

new_lines.append("\n")
new_lines.extend(button + "\n" for button in buttons)

with open(index_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

