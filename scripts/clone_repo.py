import os
import shutil
import subprocess

EXTERNAL_REPO = "https://github.com/katharinastarzer21/myst_DEDL_temp.git"
CLONE_DIR = "cookbook-gallery"
PRODUCTION_DIR = "production"
SUBFOLDERS = ["HDA", "HOOK", "STACK"]

print(f"Cloning {EXTERNAL_REPO} ...")

if os.path.exists(CLONE_DIR):
    shutil.rmtree(CLONE_DIR)

subprocess.run(["git", "clone", EXTERNAL_REPO, CLONE_DIR], check=True)

os.makedirs(PRODUCTION_DIR, exist_ok=True)

for subfolder in SUBFOLDERS:
    dst = os.path.join(PRODUCTION_DIR, subfolder)
    if os.path.exists(dst):
        print(f"Removing old {dst}")
        shutil.rmtree(dst)

    src = os.path.join(CLONE_DIR, "production", subfolder)
    if os.path.exists(src):
        print(f"Copying {subfolder} → {dst}")
        shutil.copytree(src, dst)
    else:
        print(f"Skipping {subfolder}: Not found in cloned repo.")

print("Cleaning up temporary clone")
shutil.rmtree(CLONE_DIR)

print("Selected folders in production/ were updated.")
