from tqdm import tqdm

from background_random import backgrounds
from card_load import cards
from cards_scenario import Scene
from functions import *
from global_variables import dataset_name

nb_train_cards_to_generate = 7000  # Numero di scenari da generare per l'addestramento
nb_val_cards_to_generate = 1500 # Numero di scenari da generare per la validazione
nb_test_cards_to_generate = 1500  # Numero di scenari da generare per il test

# Uscire dalla directory corrente
os.chdir('..')

# Definire i percorsi di salvataggio
train_save_dir = "model_training/"+dataset_name+"/train/images"  # Directory in cui salvare gli scenari di addestramento
val_save_dir = "model_training/"+dataset_name+"/val/images"  # Directory in cui salvare gli scenari di validazione
test_save_dir = "model_training/"+dataset_name+"/test/images"  # Directory in cui salvare gli scenari di validazione

# Creare le directory se non esistono
if not os.path.isdir(train_save_dir):
    os.makedirs(train_save_dir)
if not os.path.isdir(val_save_dir):
    os.makedirs(val_save_dir)
if not os.path.isdir(test_save_dir):
    os.makedirs(test_save_dir)

# Generare gli scenari di addestramento
for i in tqdm(range(nb_train_cards_to_generate)):
    bg = backgrounds.get_random()
    img1, card_val1, hulla1, hullb1 = cards.get_random()
    img2, card_val2, hulla2, hullb2 = cards.get_random()

    newimg = Scene(bg, img1, card_val1, hulla1, hullb1, img2, card_val2, hulla2, hullb2)
    newimg.write_files(train_save_dir)

# Generare gli scenari di validazione
for i in tqdm(range(nb_val_cards_to_generate)):
    bg = backgrounds.get_random()
    img1, card_val1, hulla1, hullb1 = cards.get_random()
    img2, card_val2, hulla2, hullb2 = cards.get_random()

    newimg = Scene(bg, img1, card_val1, hulla1, hullb1, img2, card_val2, hulla2, hullb2)
    newimg.write_files(val_save_dir)

# Generare gli scenari di test
for i in tqdm(range(nb_test_cards_to_generate)):
    bg = backgrounds.get_random()
    img1, card_val1, hulla1, hullb1 = cards.get_random()
    img2, card_val2, hulla2, hullb2 = cards.get_random()

    newimg = Scene(bg, img1, card_val1, hulla1, hullb1, img2, card_val2, hulla2, hullb2)
    newimg.write_files(test_save_dir)
