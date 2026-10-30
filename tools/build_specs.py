"""Génère shorts/NNN/short.json + meta.json à partir d'un fichier de définitions compactes.
Usage : python3 tools/build_specs.py tools/nov2_specs.py
Chaque entrée de SHORTS : (nom, publish_at, titre, costume, sources, segments)
  - publish_at : date ISO, ou un numéro de jour de décembre (série de Noël)
  - costume : dict complet, ou juste l'accessoire (bonnet + manteau de Noël)
Vérifie aussi que les mots déclencheurs existent et que les tampons ne débordent pas."""
import importlib.util, json, os, re, sys
import skia

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("specs", sys.argv[1]); mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
TITLE = skia.Typeface.MakeFromFile(f"{ROOT}/fonts/Cinzel-ExtraBold-static.ttf")
POS = [(540, 1, .56), (230, 1, .54), (850, -1, .54)]
TR = [None, "whip", None, "flash", None, "zoom"]
clean = lambda w: re.sub(r"[^\w']", "", w.lower())
problems = []
for name, when, title, costume, sources, segs in mod.SHORTS:
    if isinstance(when, int): when = f"2026-12-{when:02d}T16:00:00+01:00"
    if isinstance(costume, str): costume = {"hat": "santa", "coat": "noel", "accessory": costume}
    out = []
    for i, s in enumerate(segs):
        tts, scene, mood = s[0], s[1], s[2]; act = s[3] if len(s) > 3 else None
        last = i == len(segs) - 1
        x, face, sc = (540, 1, .62) if last else POS[i % 3]
        owl = {"x": x, "face": face, "scale": sc}
        if mood: owl["mood"] = mood
        if act: owl["acts"] = [act]
        seg = {"tts": tts, "tension": .3 if last else (.7 if scene["type"] == "verdict" else .6), "scene": scene, "owl": owl}
        if TR[i % len(TR)] and not last: seg["transition"] = TR[i % len(TR)]
        if last: seg["tail"] = .5
        toks = [clean(w) for w in tts.split()]
        for k, v in scene.items():
            if k.endswith("_on") and not any(tk.startswith(v.split("#")[0].lower()) for tk in toks): problems.append((name, i, k, v))
        if act and not any(tk.startswith(act["on"]) for tk in toks): problems.append((name, i, "act", act["on"]))
        if scene["type"] == "verdict" and skia.Font(TITLE, 130).measureText(scene["stamp"]) > 880: problems.append((name, i, "stamp trop large", scene["stamp"]))
        out.append(seg)
    d = f"{ROOT}/shorts/{name}"; os.makedirs(d, exist_ok=True)
    json.dump({"title": title.split(" ", 1)[1] if title[0] in "🎄🎃" else title, "scene_packs": [], "costume": costume,
               "segments": out, "narration": "voice_final.wav", "voice_raw": "voice_raw.mp3", "voice_tempo": 1.0,
               "voice_id": "ohItIVrXTBI80RrUECOD", "voice_name": "Guillaume"},
              open(f"{d}/short.json", "w"), ensure_ascii=False, indent=2)
    meta_p = f"{d}/meta.json"
    meta = json.load(open(meta_p)) if os.path.exists(meta_p) else {}
    meta.update({"title": title, "video": f"videos/{name}.mp4", "sources": sources, "publish_at": when,
                 "costume": ", ".join(costume.values())})
    meta.setdefault("status", "script"); meta.setdefault("voice", "à faire (Guillaume)")
    json.dump(meta, open(meta_p, "w"), ensure_ascii=False, indent=2)
    print(name, when[:16], sum(len(s[0]) for s in segs), "caractères")
print("PROBLÈMES :", problems or "aucun")
