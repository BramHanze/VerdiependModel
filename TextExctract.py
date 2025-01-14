import xml.etree.ElementTree as ET

uid = "11725393"  # Example UID
xml_file = f'data/{uid}.xml'

# Parse the XML file
tree = ET.parse(xml_file)
root = tree.getroot()

# Extract specific sections (e.g., body content)
for body in root.findall(".//body"):
    for section in body:
        text = ET.tostring(section, encoding="unicode")

print(text)
