import os
import shutil
import subprocess
import tempfile
import json

BASE_REPO = "https://github.com/katharinastarzer21/myst_DEDL_temp.git"
BASE_CLONE_DIR = "cookbook-gallery" 
PRODUCTION_DIR = "production"
CENTRAL_IMG = "img"
BASE_SUBFOLDERS = ["HDA", "HOOK", "STACK"]
REGISTRY = "cookbooks.json"

def run(cmd):
    print("➜", " ".join(cmd))
    subprocess.run(cmd, check=True)

def clean_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)

def copytree_replace(src, dst):
    
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

def copy_images_into_central(repo_dir):
    src_img = os.path.join(repo_dir, "img")
    if os.path.isdir(src_img):
        os.makedirs(CENTRAL_IMG, exist_ok=True)
        for name in os.listdir(src_img):
            s = os.path.join(src_img, name)
            d = os.path.join(CENTRAL_IMG, name)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        print(f"Copied images from {src_img} → {CENTRAL_IMG}")

def sync_base_sections():
    print(f"Cloning base repo: {BASE_REPO}")
    clean_dir(BASE_CLONE_DIR)
    run(["git", "clone", "--depth", "1", BASE_REPO, BASE_CLONE_DIR])
    os.makedirs(PRODUCTION_DIR, exist_ok=True)

    for sub in BASE_SUBFOLDERS:
        src = os.path.join(BASE_CLONE_DIR, "production", sub)
        dst = os.path.join(PRODUCTION_DIR, sub)
        if os.path.exists(src):
            print(f"↻ Updating {dst} from base repo")
            copytree_replace(src, dst)
        else:
            print(f"Skipping {sub}: not found in base repo")

    base_img = os.path.join(BASE_CLONE_DIR, "img")
    if os.path.isdir(base_img):
        copy_images_into_central(BASE_CLONE_DIR)

    print("Cleaning temp base clone")
    clean_dir(BASE_CLONE_DIR)

def sync_external_cookbooks():
    if not os.path.exists(REGISTRY):
        print(f"No {REGISTRY} found – skipping external cookbooks.")
        return

    with open(REGISTRY, "r", encoding="utf-8") as f:
        try:
            items = json.load(f)
        except Exception:
            print(f"Could not parse {REGISTRY}, skipping.")
            return

    if not isinstance(items, list) or not items:
        print(f"{REGISTRY} empty nothing to sync.")
        return

    os.makedirs(PRODUCTION_DIR, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        for it in items:
            repo_url = it.get("repo_url", "").strip()
            root = it.get("root_path", "").strip()
            if not repo_url or not root:
                print(f"Bad registry entry (missing repo_url/root_path): {it}")
                continue

            print(f"Sync external: {root} from {repo_url}")
            repo_tmp = os.path.join(tmp, root)
            run(["git", "clone", "--depth", "1", repo_url, repo_tmp])

            target = os.path.join(PRODUCTION_DIR, root)
            copytree_replace(repo_tmp, target)

            copy_images_into_central(repo_tmp)

    print("External cookbooks synced.")

def main():
    sync_base_sections()
    sync_external_cookbooks()
    print("All sources synced into production/ and img/.")

if __name__ == "__main__":
    main()
