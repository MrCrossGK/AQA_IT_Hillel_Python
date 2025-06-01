import xml.etree.ElementTree as ET


def xml_gnf():
    tree = ET.parse('groups.xml')
    root = tree.getroot()
    for group in root.findall('group'):
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None:
                print(f"Group/number: {group.find('number').text}, incoming: {incoming.text}")
            else:
                print(f"Group/number: {group.find('number').text}, incoming: Не знайдено")


if __name__ == '__main__':
    xml_gnf()
