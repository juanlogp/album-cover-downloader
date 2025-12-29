import os
import requests
import musicbrainzngs
import re

# CONFIGURACIÓN
ROOT_MUSIC_DIR = "/Users/juanlo/music/mp3"     # carpeta de tu música
COVERS_DIR = "/Users/juanlo/music/portadas"       # carpeta donde guardar TODAS las portadas

os.makedirs(COVERS_DIR, exist_ok=True)

musicbrainzngs.set_useragent(
    "AlbumArtDownloader",
    "1.0",
    "tu_email@example.com"
)

def clean_name(name):
    name = re.sub(r"^\d{4}\s*[-_]\s*", "", name) 
    name = re.sub(r"^\d{4}", "", name)          
    return name.strip()

def download_cover(artist, album):
    artist_clean = clean_name(artist)
    album_clean = clean_name(album)

    filename = f"{artist_clean} - {album_clean}.jpg"
    filename = filename.replace("/", "_")
    cover_path = os.path.join(COVERS_DIR, filename)

    if os.path.exists(cover_path):
        print(f"⏭ Ya existe: {filename}")
        return

    try:
        result = musicbrainzngs.search_releases(
            artist=artist_clean,
            release=album_clean,
            limit=5
        )

        if not result["release-list"]:
            print(f"❌ No encontrado: {artist_clean} - {album_clean}")
            return

        for release in result["release-list"]:
            release_id = release["id"]
            cover_url = f"https://coverartarchive.org/release/{release_id}/front"

            try:
                response = requests.get(cover_url, timeout=20)
                if response.status_code == 200:
                    with open(cover_path, "wb") as f:
                        f.write(response.content)
                    print(f"✔ Portada descargada: {filename}")
                    return
            except requests.exceptions.RequestException:
                continue

        print(f"⚠️ Sin portada: {artist_clean} - {album_clean}")

    except Exception as e:
        print(f"💥 Error con {artist_clean} - {album_clean}: {e}")

def scan_library():
    for artist in os.listdir(ROOT_MUSIC_DIR):
        artist_path = os.path.join(ROOT_MUSIC_DIR, artist)
        if not os.path.isdir(artist_path):
            continue

        for album in os.listdir(artist_path):
            album_path = os.path.join(artist_path, album)
            if os.path.isdir(album_path):
                download_cover(artist, album)

scan_library()

