import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element('kml', xmlns='http://www.opengis.net/kml/2.2')

# Create the Document element
document = ET.SubElement(root, 'Document')

# Create the Placemark element
placemark = ET.SubElement(document, 'Placemark')

# Create the Point element
point = ET.SubElement(placemark, 'Point')

# Create the coordinates element
coordinates = ET.SubElement(point, 'coordinates')

# Set the coordinates value to the desired latitude and longitude
latitude = 1.283
longitude = 103.833
coordinates.text = f'{longitude},{latitude}'

# Create the KML tree and write it to a file
tree = ET.ElementTree(root)
tree.write('marker.kml')
