import pandas as pd
import requests
from xml.dom.minidom import parseString, parse, Node
df = pd.read_csv('proteins.csv')

response = requests.get('https://www.uniprot.org/uniprotkb/P01024.xml')
#print(response.status_code)



# print(response.text)

with open('P01024.xml', 'w') as f:
    f.write(response.text)

document = parseString("P01024.xml")
document

elements = document.getElementsByTagName('fullName')
tagi = set([element.tagName for element in elements])
#print(tagi)
#set(map(lambda x: x.tagName, document.getElementsByTagName("*")))





"""
tags= set()
def get_tags(element):
    if element.nodeType == Node.ELEMENT_NODE:
        tags.add(element.tagName)
    
    for e in element.childNodes:
        get_all_tag_names2(e)
"""

# +


def get_tags(element):
    tags= set()
    if element.nodeType == Node.ELEMENT_NODE:
        tags.add(element.tagName)
    
    tags = tags.union(*[get_tags(e) for e in element.childNodes])
    
    return tags 

#get_tags(document)



# +
df = pd.read_csv('proteins.csv')
uniques = df['Protein'].apply(lambda x: x.split('|')[1]).unique()

response = requests.get('https://www.uniprot.org/uniprotkb/' + unique[0] + '.xml')
root = response.getroot()
sciezka = './uniprot/entry/protein/recommendedName/fullName'
elementy = root.findall(sciezka)
for element in elementy:
    print(element.text)

'''
for unique in uniques:
    response = requests.get('https://www.uniprot.org/uniprotkb/' + unique + '.xml')
    print(response.text)'''    
# -

response = requests.get('https://www.uniprot.org/uniprotkb/P01024.xml')
protein_data = response.text
document = parseString(protein_data)
document.getElementsByTagName("fullName")
document.getElementsByTagName("fullName")[0].firstChild.wholeText


def get_protein_name(unique):
    response = requests.get('https://www.uniprot.org/uniprotkb/'+unique+'.xml')
    protein_data = response.text
    document = parseString(protein_data)
    #document.getElementsByTagName("fullName")
    fullName = document.getElementsByTagName("fullName")[0].firstChild.wholeText
    
    
    return fullName


get_protein_name(document)


