"""Canonical SHA-256 for submitted claim, response or evidence bundle."""
from pathlib import Path
import hashlib, json, sys
if len(sys.argv)!=2: raise SystemExit("usage: python scripts/hash_inputs.py data.json")
value=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
canonical=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=True)
print("canonical_json =",canonical)
print("sha256 =",hashlib.sha256(canonical.encode("utf-8")).hexdigest())
