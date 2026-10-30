# Procédure hebdomadaire (tâche planifiée)

Cette procédure est suivie chaque dimanche par une session Claude planifiée. Elle produit les Shorts de la semaine, les pousse sur ce dépôt et les programme dans Metricool. Le propriétaire de la chaîne reçoit les vidéos et peut en refuser une avant sa publication.

## 0. Préparer l'environnement

- Relier le dépôt `redaprofessionnel15-spec/encre-enigmes` en écriture, le cloner, puis `pip install -r requirements.txt --break-system-packages`. Vérifier `ffmpeg -version`.
- Lire `shorts/*/meta.json` pour savoir ce qui est déjà fait, prêt ou programmé.
- La voix passe désormais par le connecteur **ElevenLabs** (plus par vidIQ). Une voix coûte environ 1 crédit par caractère (600 à 770 crédits par Short). Si un appel répond « Free generations are busy », rien n'est débité : ne pas relancer dans le même tour, programmer une reprise quelques minutes plus tard. Si les crédits manquent, faire les Shorts possibles et le signaler.
- La machine n'a que 2 processeurs : rendre les Shorts **l'un après l'autre**, jamais en parallèle.

## 1. Choisir les sujets

- Priorité à la liste d'attente ci-dessous, puis aux idées validées par vidIQ (`vidiq_keyword_research`, `vidiq_outliers` sur « histoire », « mystère », « énigme »).
- Un bon sujet : une histoire vraie, un fait surprenant énonçable en une phrase, un dénouement. Public 13-30 ans, francophone.
- Varier les époques et les lieux d'une semaine à l'autre.

Liste d'attente :

| Sujet | Costume du hibou |
|---|---|
| La Bête du Gévaudan | tricorne, manteau vert, lanterne |
| Le signal « Wow! » (1977) | casque audio, manteau blanc, radio |
| Le Manneken-Pis et ses 1 000 costumes | béret, manteau rouge |

## 2. Vérifier les faits

- Au moins deux sources sérieuses par chiffre ou date (WebSearch). En cas de désaccord entre sources, prendre la formulation prudente (« environ », « selon la légende »).
- Noter les sources dans `meta.json` (`sources`).

## 3. Écrire le script

- 45 à 52 secondes une fois lu, soit environ 120 à 135 mots.
- Ton : une histoire racontée à un ami, pas un exposé. Phrases courtes, suspense, une révélation finale.
- Accroche dans les deux premières secondes : le fait le plus surprenant d'abord.
- 7 à 9 segments ; le dernier est toujours l'appel « Abonne-toi … et laisse un like ».
- `tts` : le texte prononcé (nombres en lettres si besoin). `caption` : le texte affiché (chiffres autorisés), mêmes mots dans le même ordre.

## 4. Générer la voix

- `creative_generate_speech` (ElevenLabs), modèle `eleven_multilingual_v2`, voix George (`voice_id` `JBFqnCBsd6RMkjVDRZzb`, ou celle indiquée par `voice_id` dans `short.json`), `generations_count` 1, tout le script d'un seul tenant, sur le flow `BdaPXZcXUCpgBt9B1rZL`.
- Interroger `creative_get_flow_run_status` jusqu'à `all_completed`, puis télécharger le MP3 (`content_url`, domaine storage.googleapis.com) avec curl dans `shorts/NNN-sujet/voice_raw.mp3`.
- `voice_tempo` : 1,0 si la voix brute dure moins de 42 s, sinon 1,06. Au-delà de 58 s après resserrage, raccourcir le script plutôt que d'accélérer la voix.

## 5. Construire les scènes

- Créer `scenes/sujet.py` : 6 à 8 scènes propres au sujet, avec décors, accessoires et bruitages (voir `scenes/joconde.py` et le README).
- Chaque scène illustre ce qui est dit à ce moment ; les animations clés tombent sur les mots (`*_on`).
- Écrire `shorts/NNN-sujet/short.json` et `meta.json`.
- Faire jouer le hibou : `mood`, `pose` et 2 à 4 `acts` par Short sur les mots forts, varier les `transition`, utiliser les scènes de `scenes/common.py` quand elles conviennent (voir le README).

## 6. Contrôler avant le rendu

- `PREVIEW=t1,t2,… python3 engine.py …` sur 6 à 10 instants, puis regarder chaque image : rien ne se chevauche, texte lisible, hibou hors des sous-titres, rien dans la zone des boutons YouTube.
- Lire `alignment.txt` : chaque phrase doit tomber dans le bon segment.
- Corriger et recommencer jusqu'à ce que tout soit propre.

## 7. Rendre et vérifier

- `python3 engine.py shorts/NNN-sujet/short.json videos/NNN-sujet.mp4`.
- Vérifier : durée inférieure à 60 s, 1080×1920, son présent (`ffprobe`), quelques images extraites relues.

## 8. Publier sur le dépôt

- `git add` du dossier du Short, du pack de scènes et du MP4, commit, push sur une **branche** (jamais directement sur `main`).
- URL brute de la vidéo, épinglée sur le commit : `https://raw.githubusercontent.com/redaprofessionnel15-spec/encre-enigmes/<sha>/videos/NNN-sujet.mp4`.

## 9. Programmer dans Metricool

- Marque `7613241`, réseau YouTube, à 16 h (heure de Bruxelles) les jours prévus. Vérifier d'abord avec `getScheduledPosts` les créneaux déjà pris pour ne rien programmer en double.
- `youtubeData` : type `short`, `madeForKids` false, titre (moins de 70 caractères, avec un mot-clé), description courte avec 3 à 5 hashtags dont `#shorts`.
- Plan gratuit : 20 publications par mois au maximum.
- Mettre à jour `meta.json` (`status: "programmé"`, `publish_at`), commit, push.

## 10. Prévenir le propriétaire

- Lui envoyer les vidéos, les titres et les dates de publication dans la conversation, avec la possibilité d'en refuser une (la retirer de Metricool dans ce cas).
- Mettre à jour le tableau des Shorts dans le document de projet `claude/encre-enigmes-bible.md`.
