import os
import shutil
import subprocess
import tempfile
import json
import urllib.request

# =====================================================
# CONFIGURATION
# =====================================================

# The Lab repository (Source of Truth)
BASE_REPO = "https://github.com/katharinastarzer21/myst_DEDL_temp.git"

# Branch depends on: staging gallery => 'staging', main gallery => 'main'
BASE_REPO_BRANCH = "main"    # override in your Gallery workflow via env

BASE_CLONE_DIR = "cookbook-gallery"   # temp folder for lab clone
PRODUCTION_DIR = "production"         # where notebooks end up
CENTRAL_IMG = "img"                  # central image folder in gallery

BASE_SUBFOLDERS = ["HDA", "HOOK", "STACK"]

# The remote JSON in lab repo
REGISTRY_URL = f"https://raw.githubusercontent.com/katharinastarzer21/myst_DEDL_temp/{BASE_REPO_BRANCH}/cookbook.json"
REGISTRY = "cookbook.json"            # local downloaded registry


# =====================================================
# UTILITY HELPERS
# =====================================================

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
    """
    Collects all images from 'img/' folder of a repository into the central gallery img folder.
    """
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
        print(f"📸 Copied images from {src_img} → {CENTRAL_IMG}")


def find_subfolder(repo_root, sub):
    candidates = [
        os.path.join(repo_root, "production", sub),
        os.path.join(repo_root, sub),
    ]
    for c in candidates:
        if os.path.isdir(c):
            return c
    return None


# =====================================================
# DOWNLOAD cookbook.json FROM LAB REPO
# =====================================================

def download_registry():
    print(f"🌐 Downloading cookbook.json from:\n   {REGISTRY_URL}")
    try:
        urllib.request.urlretrieve(REGISTRY_URL, REGISTRY)
        print("✓ cookbook.json downloaded")
    except Exception as e:
        print(f"⚠️ Could not download cookbook.json: {e}")
        print("⚠️ No external cookbooks will be synced.")
        return False
    return True


# =====================================================
# SYNC INTERNAL NOTEBOOKS (HDA, HOOK, STACK)
# =====================================================

def sync_base_sections():
    print(f"📦 Cloning Lab repo: {BASE_REPO} (branch: {BASE_REPO_BRANCH})")
    clean_dir(BASE_CLONE_DIR)

    run([
        "git", "clone",
        "--depth", "1",
        "--single-branch",
        "--branch", BASE_REPO_BRANCH,
        BASE_REPO,
        BASE_CLONE_DIR
    ])

    os.makedirs(PRODUCTION_DIR, exist_ok=True)

    for sub in BASE_SUBFOLDERS:
        src = find_subfolder(BASE_CLONE_DIR, sub)
        dst = os.path.join(PRODUCTION_DIR, sub)
        if src:
            print(f"↻ Updating internal section: {dst}")
            copytree_replace(src, dst)
        else:
            print(f"⚠️ Skipping {sub}: folder not found in Lab repo branch {BASE_REPO_BRANCH}")

    copy_images_into_central(BASE_CLONE_DIR)

    print("🧹 Cleaning Lab clone folder")
    clean_dir(BASE_CLONE_DIR)


# =====================================================
# SYNC EXTERNAL COOKBOOKS FROM registry
# =====================================================

def sync_external_cookbooks():

    # Download remote cookbook.json
    if not download_registry():
        return  # no external cookbooks

    if not os.path.exists(REGISTRY):
        print("⚠️ No cookbook.json found — skipping external syncing.")
        return

    try:
        with open(REGISTRY, "r", encoding="utf-8") as f:
            items = json.load(f)
    except Exception as e:
        print(f"⚠️ Could not parse cookbook.json: {e}")
        return

    if not isinstance(items, list) or not items:
        print("ℹ️ cookbook.json is empty — no external cookbooks to sync.")
        return

    os.makedirs(PRODUCTION_DIR, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        for it in items:
            repo_url = (it.get("repo_url") or "").strip()
            root = (it.get("root_path") or "").strip()
            branch = (it.get("branch") or "").strip()

            if not repo_url or not root:
                print(f"⚠️ Invalid entry in cookbook.json: {it}")
                continue

            print(f"🌐 Sync external cookbook: {root} from {repo_url} (branch: {branch or 'default'})")
            repo_tmp = os.path.join(tmp, root)

            clone_cmd = ["git", "clone", "--depth", "1"]
            if branch:
                clone_cmd += ["--single-branch", "--branch", branch]
            clone_cmd += [repo_url, repo_tmp]

            run(clone_cmd)

            src_path = os.path.join(repo_tmp, root) if root not in (".", "/") else repo_tmp

            target = os.path.join(PRODUCTION_DIR, root)

            if os.path.exists(src_path):
                copytree_replace(src_path, target)
            else:
                copytree_replace(repo_tmp, target)

            copy_images_into_central(repo_tmp)

    print("✓ All external cookbooks synced.")


# =====================================================
# MAIN
# =====================================================

def main():
    print("\n========== SYNCING NOTEBOOK GALLERY ==========\n")
    sync_base_sections()
    sync_external_cookbooks()
    print("\n✓ All sources synced into production/ and img/\n")


if __name__ == "__main__":
    main()
