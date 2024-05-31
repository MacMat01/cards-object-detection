xml_body_1 = """<annotation>
        <folder>FOLDER</folder>
        <filename>{FILENAME}</filename>
        <path>{PATH}</path>
        <source>
                <database>Unknown</database>
        </source>
        <size>
                <width>{WIDTH}</width>
                <height>{HEIGHT}</height>
                <depth>3</depth>
        </size>
"""
xml_object = """ <object>
                <name>{CLASS}</name>
                <pose>Unspecified</pose>
                <truncated>0</truncated>
                <difficult>0</difficult>
                <bndbox>
                        <xmin>{XMIN}</xmin>
                        <ymin>{YMIN}</ymin>
                        <xmax>{XMAX}</xmax>
                        <ymax>{YMAX}</ymax>
                </bndbox>
        </object>
"""
xml_body_2 = """</annotation>        
"""

from hull import *


def create_voc_xml(xml_file, img_file, listbba, display=False):
    with open(xml_file, "w") as f:
        f.write(xml_body_1.format(
            **{'FILENAME': os.path.basename(img_file), 'PATH': img_file, 'WIDTH': imgW, 'HEIGHT': imgH}))
        for bba in listbba:
            f.write(xml_object.format(
                **{'CLASS': bba.classname, 'XMIN': bba.x1, 'YMIN': bba.y1, 'XMAX': bba.x2, 'YMAX': bba.y2}))
        f.write(xml_body_2)
        if display: print("New xml", xml_file)
