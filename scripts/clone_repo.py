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

if os.path.exists(PRODUCTION_DIR):
    print(f"🧹 Removing old {PRODUCTION_DIR}/ directory ...")
    shutil.rmtree(PRODUCTION_DIR)

os.makedirs(PRODUCTION_DIR, exist_ok=True)

for subfolder in SUBFOLDERS:
    src = os.path.join(CLONE_DIR, "production", subfolder)
    dst = os.path.join(PRODUCTION_DIR, subfolder)
    if os.path.exists(src):
        print(f"Copying {subfolder} → {dst}")
        shutil.copytree(src, dst)
    else:
        print(f"kipping {subfolder}: Not found in cloned repo.")

print("Cleaning up temporary clone")
shutil.rmtree(CLONE_DIR)

print("production/ is now updated from external repo.")
