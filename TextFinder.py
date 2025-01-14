from Bio import Entrez

def uidfinder():
    Entrez.email = "bram.koobs11@gmail.com"
    search_handle = Entrez.esearch(db="pmc", term="cancer", retmax=5)
    search_results = Entrez.read(search_handle)
    uids = search_results["IdList"]
    return uids

uids = ['11725393', '11725380', '11725367', '11725365', '11725361']

def uidfetcher(uids):
    for uid in uids:
        fetch_handle = Entrez.efetch(db="pmc", id=uid, rettype="full", retmode="xml")
        record = fetch_handle.read()
        
        with open(f'data/{uid}.xml', 'wb') as file:
            file.write(record)

uids = ['11725393']

#uids = uidfinder()
#print(uids, '\n')
uidfetcher(uids)

import xml.etree.ElementTree as ET

uid = "11725393"  # Example UID
xml_file = f'data/{uid}.xml'

# Parse the XML file
tree = ET.parse(xml_file)
root = tree.getroot()


# Extract specific sections (e.g., body content)
for body in root.findall(".//body"):
    print("Article Body Content:\n")
    for section in body:
        print(ET.tostring(section, encoding="unicode"))
