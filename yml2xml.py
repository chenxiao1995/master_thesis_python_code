from xml.dom.minidom import Document,parseString
from xml.etree.ElementTree import Element, SubElement, tostring
from dicttoxml import dicttoxml
import glob
import yaml

anno_yaml_pfad='/Volumes/xiao_ssd/data/MobilityAids/Annotations_RGB_TestSet2/'
anno_xml_pfad='/Volumes/xiao_ssd/data/MobilityAids/label_test/'


for files in glob.glob(anno_yaml_pfad+'*.yml'):

    # Read the YAML file
        with open(files) as inf:
          root=yaml.load(inf)
          xml=dicttoxml(root)
          dom = parseString(xml)
          dom2prettyxml=dom.toprettyxml()

    # Output back XML
        with open(anno_xml_pfad+files.split('/')[-1][:-3] + "xml", "w") as outf:
          #xmlplain.xml_from_obj(root, outf, pretty=True)
          outf.write(dom2prettyxml)
          outf.close