__author__ = 'zhaicao'

import xml.etree.ElementTree as ET

if __name__ == "__main__":
    tree = ET.parse('hosts.xml')
    root = tree.getroot()
    for i in root.find('hosts'):
        print("%s, %s" % (i[0].text, i[17][0][3].text))


