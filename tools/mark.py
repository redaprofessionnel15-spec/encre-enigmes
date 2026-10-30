"""python3 tools/mark.py NOM youtube=ID tiktok=1 ..."""
import json, sys
n = sys.argv[1]; p = f"shorts/{n}/meta.json"; m = json.load(open(p))
for kv in sys.argv[2:]:
    k, v = kv.split("=", 1); m[k] = v
m["status"] = "programmé"
json.dump(m, open(p, "w"), ensure_ascii=False, indent=2); print(n, {k: m.get(k) for k in ("youtube", "tiktok", "publish_at")})
