import tarfile

tar = tarfile.open("data/dtd_raw/dtd-r1.0.1.tar.gz")
tar.extractall()
tar.close()

print("File estratto con successo.")
