import os
import shutil
import subprocess

EXTERNAL_REPO = "https://github.com/katharinastarzer21/myst_DEDL_temp.git"
CLONE_DIR = "cookbook-gallery"
PRODUCTION_DIR = "production"
SUBFOLDERS = ["HDA", "HOOK", "STACK"]


print(f"Cloning {EXTERNAL_REPO} ...")
subprocess.run(["git", "clone", EXTERNAL_REPO, CLONE_DIR], check=True)

os.makedirs(PRODUCTION_DIR, exist_ok=True)

for subfolder in SUBFOLDERS:
    #src = os.path.join(CLONE_DIR, subfolder)
    src = os.path.join(CLONE_DIR, "production", subfolder)
    dst = os.path.join(PRODUCTION_DIR, subfolder)
    if os.path.exists(src):
        print(f"Copying {subfolder} → {dst}")
        os.makedirs(dst, exist_ok=True)
        # Inhalte kopieren
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
    else:
        print(f"kipping {subfolder}: Not found in cloned repo.")

# === Clone-Repo entfernen ===
print("Cleaning up temporary clone")
shutil.rmtree(CLONE_DIR)

print("Done.")
