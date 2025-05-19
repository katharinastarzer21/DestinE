import yaml
import sys
import os

preview_mode = "--preview" in sys.argv

# Load gallery YAML only if not in preview
if not preview_mode:
    gallery_path = "notebook_gallery.yaml"
    if os.path.exists(gallery_path):
        with open(gallery_path) as f:
            gallery = yaml.safe_load(f)
    else:
        gallery = {"domains": {}}


with open('issue_body.txt') as f:
    body = f.read()

print("Full Issue Body:")
print(body)

fields = {
    "Repository URL": "",
    "Cookbook Title": "",
    "Short Description": "",
    "Thumbnail Image URL": "",
    "Root Path Name": ""
}

lines = body.splitlines()

current_label = None
for line in lines:
    line = line.strip().lstrip("#").strip()
    if line in fields:
        current_label = line
    elif current_label and line:
        fields[current_label] = line
        current_label = None

repo_url = fields["Repository URL"]
title = fields["Cookbook Title"]
description = fields["Short Description"]
thumbnail = fields["Thumbnail Image URL"]
root_path = fields["Root Path Name"]

print(f"Repo URL: {repo_url}")
print(f"Title: {title}")
print(f"Description: {description}")
print(f"Thumbnail: {thumbnail}")
print(f"Root Path: {root_path}")

if not root_path:
    raise ValueError("Root Path konnte nicht extrahiert werden – Abbruch.")

# Update gallery YAML only if NOT preview
if not preview_mode:
    gallery['domains'][root_path] = {
        'title': title,
        'branch': 'main',
        'root_path': root_path,
        'description': description,
        'thumbnail': thumbnail,
        'url': f"https://katharinastarzer21.github.io/DestinE/cookbooks/{root_path}/index.html"
    }

    with open('notebook_gallery.yaml', 'w') as f:
        yaml.dump(gallery, f, sort_keys=False)

# Export values to GitHub Actions
with open(os.environ['GITHUB_ENV'], 'a') as env_file:
    env_file.write(f"REPO_URL={repo_url}\n")
    env_file.write(f"ROOT_PATH={root_path}\n")
