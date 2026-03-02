# Run THIS locally and in CI to compare hashes
# Make sure the path is EXACTLY the same notebook

import hashlib
from pathlib import Path

nb_path = Path("production/HDA/EUM_data/DEDL-HDA-EO.EUM.DAT.METOP.AVHRRL1.ipynb")

if not nb_path.exists():
    print("ERROR: Notebook not found at", nb_path)
else:
    data = nb_path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    print("File:", nb_path)
    print("Size (bytes):", len(data))
    print("SHA256:", sha)

# --- OPTIONAL: count outputs as well ---
import json
nb = json.loads(nb_path.read_text(encoding="utf-8"))

cells_with_outputs = sum(1 for c in nb.get("cells", []) if c.get("outputs"))
png_outputs = sum(
    1
    for c in nb.get("cells", [])
    for o in c.get("outputs", [])
    if "image/png" in o.get("data", {})
)

print("cells_with_outputs:", cells_with_outputs)
print("png_outputs:", png_outputs)
