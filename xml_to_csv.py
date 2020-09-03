import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     float(member[4][0].text),
                     float(member[4][1].text),
                     float(member[4][2].text),
                     float(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df
def xml_to_csv_2(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()[0]
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[2].text),
                     int(root.find('size')[1].text),
                     member[0][1].text,
                     float(member[0][0][2].text),
                     float(member[0][0][4].text),
                     float(member[0][0][1].text),
                     float(member[0][0][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

if __name__ == '__main__':
    try:
        # image_path = os.path.join(os.getcwd(), 'train_annotation/')
        key='f3'
        path="/Volumes/xiao_ssd/20200813_testdaten/f_regenshirm/"
        label_path=os.path.join(path,key+'_label')
        output = os.path.join(path, 'data')
        if not os.path.exists(output):
            os.mkdir(output)
        output_path=os.path.join(output,key+'.csv')
        xml_df = xml_to_csv(label_path)
        xml_df.to_csv(output_path, index=None)
        print('Successfully converted xml to csv.')
    except SystemExit:
        pass

