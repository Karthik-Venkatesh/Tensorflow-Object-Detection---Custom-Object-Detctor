import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        outputs = ET.Element('outputs')
        obj = ET.SubElement(outputs ,'object')
        item = ET.SubElement(obj ,'item')
        a = urlparse(root.find('path').text)
        base_name = os.path.basename(a.path)
        for member in obj:
            value = (base_name,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     root[1][0][0][0].text,
                     int(root[1][0][0][1][0].text),
                     int(root[1][0][0][1][1].text),
                     int(root[1][0][0][1][2].text),
                     int(root[1][0][0][1][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for directory in ['train', 'test']:
        image_path = os.path.join(os.getcwd(), 'images/{}'.format(directory))
        print(image_path)
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('data/{}.csv'.format(directory), index=None)
    print('Successfully converted xml to csv.')
    


main()