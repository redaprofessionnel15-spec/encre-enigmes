#!/bin/bash
# Copie < 10 Mo pour l'envoi via le navigateur (YouTube Studio et TikTok).
for n in "$@"; do
  vd=$(ffprobe -v error -show_entries format=duration -of csv=p=0 videos/$n.mp4)
  vb=$(python3 -c "print(int(min(2500, 9.3*8*1000/$vd - 140)))")
  ffmpeg -y -loglevel error -i videos/$n.mp4 -c:v libx264 -preset veryfast -b:v ${vb}k -maxrate ${vb}k -bufsize $((vb*2))k -c:a aac -b:a 128k tiktok/$n.mp4
  echo "$n $(stat -c %s tiktok/$n.mp4)"
done
