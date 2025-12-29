# Album Cover Downloader (MP3)

Script en **Python** que recorre una biblioteca de música organizada por **Artista / Álbum** y descarga automáticamente las **portadas de los discos** desde internet, guardándolas todas en una carpeta llamada `portadas`.

✔ Seguro de ejecutar varias veces  
✔ Solo descarga álbumes nuevos  
✔ No modifica los archivos MP3  
✔ Usa fuentes abiertas (MusicBrainz + Cover Art Archive)

## Estructura de carpetas esperada

Música/Artista/Album


Ejemplo:

Música/Metallica/Kill 'Em All/

Música/Foo Fighters/Wasting Light/


## Requisitos

- macOS o Linux
- Python **3.9+**
- Biblioteca organizada por carpetas

Comprueba Python:

`python3 --version`

## Instalación

1- Clonar el repositorio

`git clone https://github.com/juanlogp/album-cover-downloader.git
cd album-cover-downloader`

2- Crear entorno virtual (recomendado)

`python3 -m venv venv
source venv/bin/activate`

Cuando esté activo verás:

(venv)

3- Instalar dependencias

`pip install musicbrainzngs requests`

## Uso

1- Edita la variable ROOT_MUSIC_DIR en el script)

2-Ejecuta:

`python descargar_portadas.py`

## Resultado

Se creará una carpeta portadas/ con una imagen por álbum:

Metallica - Kill 'Em All.jpg

## Personalización

Dentro de descargar_portadas.py puedes modificar:

ROOT_MUSIC_DIR = ruta carpeta música
COVERS_DIR = ruta a carpeta portadas

---

- Ejecuciones repetidas:
	Puedes ejecutar el script tantas veces como quieras:
	Si la portada ya existe → se ignora
	Si detecta un álbum nuevo → se descarga
	No sobrescribe archivos existentes

---

## Notas importantes
- Los nombres de carpetas deben parecerse al nombre real del álbum
- Algunos álbumes tienen varias ediciones
- La primera edición encontrada puede no tener portada
- Las búsquedas con acentos o años pueden fallar


## Fuentes de datos
MusicBrainz — https://musicbrainz.org/
Cover Art Archive — https://coverartarchive.org/





†
