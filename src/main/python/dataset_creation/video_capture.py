import os
import time

import cv2

# Crea la cartella video se non esiste
if not os.path.exists('data/video'):
    os.makedirs('data/video')

# Apri il video capture
cap = cv2.VideoCapture(0)

# Imposta la risoluzione del video
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Imposta il codec e crea un oggetto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Modifica il codec a 'mp4v' per i file .mp4

video_counter = 0

while True:
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # Premi 's' per iniziare la registrazione
            print(f"Registrazione del video {video_counter} in corso...")
            out = cv2.VideoWriter('data/video/output{}.mp4'.format(video_counter), fourcc, 20.0,
                                  (1280, 720))  # Modifica l'estensione del file a .mp4
            start_time = time.time()
            while (int(time.time() - start_time) < 20):
                ret, frame = cap.read()
                if ret == True:
                    # scrivi il frame nel file di output
                    out.write(frame)

                    # mostra il frame
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            # Chiudi il file di output
            out.release()
            print(f"Video {video_counter} salvato.")
            video_counter += 1
        elif key == ord('q'):
            break
    else:
        break

# Chiudi il video capture e le finestre
cap.release()
cv2.destroyAllWindows()
