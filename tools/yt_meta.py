"""Ajoute à chaque meta.json : yt_title, yt_description, yt_tags (pour YouTube Studio / TikTok)."""
import json, glob, re, sys
BASE = ["histoire", "mystère", "encre et énigmes"]
for f in sorted(glob.glob("shorts/*/meta.json")):
    m = json.load(open(f)); s = json.load(open(f.replace("meta.json", "short.json")))
    if m.get("status") not in ("script", "voix", "rendu") and "yt_title" in m: continue
    pa = m.get("publish_at", "")
    if pa < "2026-11-01": continue
    hook = s["segments"][0]["tts"]
    month = pa[5:7]; day = int(pa[8:10]) if pa else 0
    if month == "12": tag = "#noel"; extra = ["noël"]
    elif month == "11" and day <= 9: tag = "#halloween"; extra = ["halloween"]
    else: tag = "#histoireinsolite"; extra = ["histoire insolite"]
    m["yt_title"] = m["title"][:95]
    m["yt_description"] = f"{hook} 🦉 Une énigme de l'histoire chaque jour sur Encre & Énigmes.\n\n#shorts #histoire {tag} #mystere"
    m["yt_tags"] = ", ".join(extra + BASE) + ","
    json.dump(m, open(f, "w"), ensure_ascii=False, indent=2)
print("ok")
