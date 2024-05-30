import os
import shutil

directories = {
    "train": ("data/scenes/train/images", "data/scenes/train/labels"),
    "val": ("data/scenes/val/images", "data/scenes/val/labels"),
    "test": ("data/scenes/test/images", "data/scenes/test/labels")
}

def move_txt_files(source_dir, destination_dir):
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir)

    for file_name in os.listdir(source_dir):
        if file_name.endswith(".txt"):
            source = os.path.join(source_dir, file_name)
            destination = os.path.join(destination_dir, file_name)
            shutil.move(source, destination)

for key in directories:
    move_txt_files(directories[key][0], directories[key][1])