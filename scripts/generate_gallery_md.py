import os
import shutil
import subprocess

EXTERNAL_REPO = "https://github.com/katharinastarzer21/myst_DEDL_temp.git"
CLONE_DIR = "cookbook-gallery"
PRODUCTION_DIR = "production"
SUBFOLDERS = ["HDA", "HOOK", "STACK"]

print(f"📥 Cloning {EXTERNAL_REPO} ...")

if os.path.exists(CLONE_DIR):
    shutil.rmtree(CLONE_DIR)

subprocess.run(["git", "clone", EXTERNAL_REPO, CLONE_DIR], check=True)

os.makedirs(PRODUCTION_DIR, exist_ok=True)

for subfolder in SUBFOLDERS:
    path = os.path.join(PRODUCTION_DIR, subfolder)
    if os.path.exists(path):
        print(f"🧹 Removing {path}")
        shutil.rmtree(path)

for subfolder in SUBFOLDERS:
    src = os.path.join(CLONE_DIR, "production", subfolder)
    dst = os.path.join(PRODUCTION_DIR, subfolder)
    if os.path.exists(src):
        print(f"Copying {src} → {dst}")
        shutil.copytree(src, dst)
    else:
        print(f"Skipping {subfolder}: Not found in cloned repo.")

print("Cleaning up temporary clone")
shutil.rmtree(CLONE_DIR)

print("Selected subfolders in production/ are now updated.")
