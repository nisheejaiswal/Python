import xml.etree.ElementTree as ET

data = '''
  <data>
    <person>
        <name> Aakash </name>
        <phone type = "national">
            8260555991
        </phone>
    </person>
    <person>
        <name> Aakash </name>
        <phone type = "national">
            8260555991
        </phone>
    </person>
   </data>
    '''

tree = ET.fromstring(data)

print("Attr: ", tree.find('phone').get('type'))
