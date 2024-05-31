import os
import glob

directories = ["data/scenes/train/images", "data/scenes/val/images", "data/scenes/test/images"]

def delete_xml_files(directory):
    # Get all XML files in the directory
    xml_files = glob.glob(os.path.join(directory, '*.xml'))

    # Delete each XML file
    for xml_file in xml_files:
        os.remove(xml_file)
        print(f"File {xml_file} removed successfully")

# Use the function on your directories
for directory in directories:
    delete_xml_files(directory)