import json
from yt_dlp import YoutubeDL

CHANNEL_SHORTS_URL = "https://www.youtube.com/@DerielServicios/shorts"
OUTPUT = "youtube-videos.json"

opts = {
    "extract_flat": True,
    "playlistend": 12,
    "quiet": True,
    "no_warnings": True,
    "ignoreerrors": True,
}

videos = []
with YoutubeDL(opts) as ydl:
    info = ydl.extract_info(CHANNEL_SHORTS_URL, download=False)
    for entry in (info or {}).get("entries", []):
        if not entry:
            continue
        video_id = entry.get("id")
        if not video_id:
            continue
        videos.append({
            "id": video_id,
            "title": entry.get("title") or "Short de Deriel",
            "category": "YouTube Short",
            "url": "https://www.youtube.com/shorts/" + video_id,
            "thumbnail": "https://i.ytimg.com/vi/" + video_id + "/hqdefault.jpg",
        })

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(videos, f, ensure_ascii=False, indent=2)

print(f"Se guardaron {len(videos)} Shorts en {OUTPUT}")
