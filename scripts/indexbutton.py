import os

tag_gallery_dir = "galleries_by_tag"
gallery_dirs = ["galleries", "galleries_by_tag"]  
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

def make_buttons_block(base_dir: str):
    
    rel_to_tags = os.path.relpath(tag_gallery_dir, start=base_dir or ".")
    return [
        f"{button_prefix}"
        f"{fname.replace('tag-', '').replace('.md', '').replace('-', ' ').title()} "
        f"<{os.path.join(rel_to_tags, fname).replace(os.sep, '/')}>"
        f"{button_suffix}\n"
        for fname in tag_files
    ]

def update_file(file_path):
    """Fügt die Buttons nach dem Marker ein, ersetzt bestehende Buttons."""
    if not os.path.isfile(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    try:
        marker_idx = next(i for i, ln in enumerate(lines) if ln.strip() == start_marker)
    except StopIteration:
        print(f"Marker '{start_marker}' not found in {file_path}, skipping.")
        return

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

    base_dir = os.path.dirname(file_path) or "."
    new_buttons_block = make_buttons_block(base_dir)

    replacement = ["\n"] + new_buttons_block + ["\n"]
    new_lines = lines[:start_idx] + replacement + lines[end_idx:]

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"Updated buttons in {file_path}")

update_file("index.md")

for gallery_dir in gallery_dirs:
    if not os.path.isdir(gallery_dir):
        continue
    for md_file in os.listdir(gallery_dir):
        if md_file.endswith(".md"):
            update_file(os.path.join(gallery_dir, md_file))
