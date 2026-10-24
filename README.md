# Encre & Énigmes

Moteur de Shorts animés de la chaîne YouTube **Encre & Énigmes** (@EncreEtEnigmes) : histoire et mystères racontés en moins de 60 secondes par un hibou conteur dont le costume change à chaque épisode.

Tout est généré par code : images (Skia, 1080×1920, 30 i/s), musique et bruitages (synthèse), sous-titres karaoké, synchronisation des lèvres. Seule la voix vient d'ElevenLabs (voix « George », via vidIQ).

## Arborescence

```
engine.py          moteur de rendu (spec JSON -> MP4)
character.py       le hibou : costumes, humeurs, gestes, plume
tighten_voice.py   resserre les pauses de la voix et l'accélère un peu
scenes/            un « pack de scènes » par Short (décors, accessoires, sons propres au sujet)
fonts/             Cinzel, Cormorant, Inter (licence OFL)
brand/             photo de profil, bannière
shorts/NNN-sujet/  short.json (script + scènes), voice_raw.mp3 (voix George), meta.json (titre, statut, date)
videos/            MP4 finaux, servis en URL brute pour la planification
AUTOMATION.md      la procédure hebdomadaire complète
```

## Rendre un Short

```bash
pip install -r requirements.txt      # + ffmpeg installé sur la machine
python3 engine.py shorts/002-joconde/short.json videos/002-joconde.mp4
```

- Si `voice_final.wav` n'existe pas, le moteur le fabrique depuis `voice_raw.mp3` avec `tighten_voice.py` (tempo `voice_tempo`, 1,06 par défaut).
- Aperçu rapide sans vidéo : `PREVIEW=3.0,20.0 python3 engine.py spec.json x.mp4` écrit des images fixes dans `x_work/`.
- `x_work/alignment.txt` montre le calage de chaque phrase sur la voix : c'est la première chose à vérifier.
- Les modèles Kokoro (voix de secours locale) sont facultatifs quand il y a une narration : le moteur n'utilise alors que le phonémiseur espeak, ce qui donne exactement le même calage.

## Format d'un `short.json`

```json
{
  "title": "…",
  "narration": "voice_final.wav",
  "voice_raw": "voice_raw.mp3",
  "voice_tempo": 1.06,
  "scene_packs": ["scenes/joconde.py"],
  "costume": {"hat": "detective", "coat": "brown", "accessory": "magnifier"},
  "segments": [
    {
      "tts": "texte exactement tel qu'il est prononcé",
      "caption": "texte affiché (chiffres, ponctuation)",
      "tension": 0.5,
      "scene": {"type": "wall", "slam_on": "vide"},
      "owl": {"x": 540, "face": 1, "scale": 0.56}
    }
  ]
}
```

- `*_on` : mot (ou `mot#n` pour la n-ième occurrence) sur lequel une animation ou un son se déclenche.
- Costumes : chapeaux `bicorne tricorne detective headphones beret crown`, manteaux `navy brown green red white black`, accessoires `spyglass magnifier lantern radio`.
- Scènes génériques (dans `engine.py`) : `hook place scroll battle toll finale cta throne`. Le dernier segment est toujours `cta` (abonnement + like).

## Écrire un pack de scènes

Un pack est un fichier Python chargé par `exec` dans les globales du moteur. Il a donc accès à tous les outils de dessin (`P`, `lin`, `rad`, `text_c`, `gold`, `fit`, `font`, `eo`, `eback`, `word_time`…) et de son (`put`, `boom`, `whoosh`, `thud`, `tick`, `pop`, `bell`, `taiko`, `riser`…).

1. Définir des fonctions `sc_xxx(cv, p, lt, dur, si, t)` qui dessinent la scène et renvoient les indications pour le hibou (`look`, `surprise`, `mood`, `point`).
2. Les enregistrer : `SCENES.update(xxx=sc_xxx, …)`.
3. Ajouter les bruitages : une fonction `hook(si, seg, p, a_, b_, ty)` puis `SFX_HOOKS.append(hook)`.

Voir `scenes/joconde.py` pour un exemple complet.

## Règles de mise en page

- Zone sûre : rien d'important sous y = 1550 ni à droite de x = 960 (boutons YouTube).
- Sous-titres à y = 1150 ; le hibou se déplace entre les scènes pour ne jamais les couvrir.
- Ponctuation française collée par espace insécable (« ! », « ? », « : »).
