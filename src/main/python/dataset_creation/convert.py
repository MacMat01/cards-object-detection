import os
import subprocess

def create_dir_if_not_exists(directory):
    if not os.path.isdir(directory):
        os.makedirs(directory)

def run_command(command):
    subprocess.run(command)

directories = ["data/scenes/train/", "data/scenes/val/", "data/scenes/test/"]
commands = [
    ["python", "convert_voc_yolo.py", "data/scenes/train/images", "data/cards.names"],
    ["python", "convert_voc_yolo.py", "data/scenes/val/images", "data/cards.names"],
    ["python", "convert_voc_yolo.py", "data/scenes/test/images", "data/cards.names"],
    ["python", "create_labels_dir.py"],
    ["python", "delete_xml.py"]
]

for directory in directories:
    create_dir_if_not_exists(directory)

for command in commands:
    run_command(command)