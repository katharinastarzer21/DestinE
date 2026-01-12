import os
import json

ISSUE_BODY_FILE = "issue_body.txt"
REGISTRY = "cookbooks.json"

def norm(s: str) -> str:
    """Normalize strings for safe matching."""
    return (s or "").strip().upper()

def load_issue_body() -> str:
    with open(ISSUE_BODY_FILE, encoding="utf-8") as f:
        return f.read()

def parse_fields(body: str) -> dict:
    # expects headings like:
    # Repository URL
    # Cookbook Title in capital letters
    fields = {
        "Repository URL": "",
        "Cookbook Title in capital letters": "",
    }

    lines = body.splitlines()
    current_label = None

    for line in lines:
        line = line.strip().lstrip("#").strip()
        if line in fields:
            current_label = line
            continue
        if current_label and line:
            fields[current_label] = line.strip()
            current_label = None

    repo_url = (fields["Repository URL"] or "").strip()
    root_path = (fields["Cookbook Title in capital letters"] or "").strip()
    return {"repo_url": repo_url, "root_path": root_path}

def get_labels() -> set[str]:
    labels_raw = os.getenv("ISSUE_LABELS", "")
    labels = {x.strip() for x in labels_raw.split(",") if x.strip()}
    return labels

def load_registry() -> list[dict]:
    if not os.path.exists(REGISTRY):
        return []
    try:
        with open(REGISTRY, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        print("WARNING: cookbooks.json is not a list; resetting to [].")
        return []
    except Exception as e:
        print(f"WARNING: Could not read cookbooks.json ({e}); resetting to [].")
        return []

def save_registry(registry: list[dict]) -> None:
    with open(REGISTRY, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

def write_env(**kv) -> None:
    github_env = os.environ.get("GITHUB_ENV")
    if not github_env:
        print("WARNING: GITHUB_ENV not set; skipping env export.")
        return
    with open(github_env, "a", encoding="utf-8") as env_file:
        for k, v in kv.items():
            env_file.write(f"{k}={v}\n")

def main():
    body = load_issue_body()
    print("Full Issue Body:")
    print(body)

    fields = parse_fields(body)
    repo_url = (fields["repo_url"] or "").strip()
    root_path_raw = (fields["root_path"] or "").strip()

    root_path = norm(root_path_raw)

    print("Extracted Fields:")
    print(f"→ Repo URL  : {repo_url}")
    print(f"→ Root Path : {root_path_raw}  (normalized: {root_path})")

    if not root_path:
        raise ValueError("ERROR: Root Path could not be extracted. Aborting.")

    labels = get_labels()
    print(f"ISSUE_LABELS: {sorted(labels)}")

    is_add = "add-repo" in labels
    is_remove = "remove-repo" in labels

    # Safety: must be exactly one of them
    if is_add and is_remove:
        raise ValueError("ERROR: Both add-repo and remove-repo are set. Choose only one.")
    if not (is_add or is_remove):
        raise ValueError("ERROR: Neither add-repo nor remove-repo label found. Nothing to do.")

    if is_add and not repo_url:
        raise ValueError("ERROR: REPO_URL is required for add-repo but is empty.")

    action = "add" if is_add else "remove"

    if action == "add":
        write_env(REPO_URL=repo_url, ROOT_PATH=root_path, COOKBOOK_ACTION=action)
    else:
        write_env(ROOT_PATH=root_path, COOKBOOK_ACTION=action)

    registry = load_registry()

    before = len(registry)
    registry = [e for e in registry if norm(e.get("root_path")) != root_path]
    removed = before - len(registry)

    if action == "remove":
        print(f"Action=remove. Removed {removed} entries for root_path='{root_path}'.")
    else:
        registry.append({"repo_url": repo_url, "root_path": root_path})
        print(f"Action=add. Upserted entry for root_path='{root_path}'.")

    save_registry(registry)

    print(f"Updated {REGISTRY}. Action: {action}")
    print("Registry root_paths now:", [norm(e.get("root_path")) for e in registry])

if __name__ == "__main__":
    main()
