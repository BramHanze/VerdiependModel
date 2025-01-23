from Bio import Entrez
import time

def uidfinder():
    Entrez.email = 'bram.koobs11@gmail.com'
    Entrez.api_key = '1e3618cf8085ceaaa4cec35608f05ae72d09'
    search_handle = Entrez.esearch(db="pmc", term="cancer", retmax=100)
    search_results = Entrez.read(search_handle)
    uids = search_results['IdList']
    return uids


def uidfetcher(uids):
    for uid in uids:
        fetch_handle = Entrez.efetch(db='pmc', id=uid, rettype='full', retmode='xml')
        record = fetch_handle.read()
        
        with open(f'data/{uid}.xml', 'wb') as file:
            file.write(record)
        time.sleep(0.1) #wait 100ms, the key allows for 10 request/sec

uids = ['11725393']

uids = uidfinder()
#print(uids, '\n')
uidfetcher(uids)
