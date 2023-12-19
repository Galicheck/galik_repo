import pandas as pd
import requests
from xml.dom.minidom import parse, Node
df = pd.read_csv('proteins.csv')

response = requests.get('https://www.uniprot.org/uniprotkb/P01024.xml')
#print(response.status_code)

#print(response.text)

with open('P01024.xml', 'w') as f:
    f.write(response.text)

document = parse("P01024.xml")

elements = document.getElementsByTagName('*')
tagi = set([element.tagName for element in elements])

# set(map(lambda x: x.tagName, document.getElementsByTagName("*")))




"""
tags= set()
def get_tags(element):
    if element.nodeType == Node.ELEMENT_NODE:
        tags.add(element.tagName)
    
    for e in element.childNodes:
        get_all_tag_names2(e)
"""

"""

def get_tags(element):
    tags= set()
    if element.nodeType == Node.ELEMENT_NODE:
        tags.add(element.tagName)
    
    tags = tags.union(*[get_tags(e) for e in element.childNodes])
    
    return tags 



"""

