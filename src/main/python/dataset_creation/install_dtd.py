import requests
import os

url = "https://www.robots.ox.ac.uk/~vgg/data/dtd/download/dtd-r1.0.1.tar.gz"
response = requests.get(url, stream=True)

# Scegli la cartella di destinazione
dest_folder = "data/dtd_raw"

# Assicurati che la cartella esista
os.makedirs(dest_folder, exist_ok=True)

# Crea il percorso completo del file
file_path = os.path.join(dest_folder, "dtd-r1.0.1.tar.gz")

with open(file_path, "wb") as out_file:
    out_file.write(response.content)

print("File scaricato con successo.")
