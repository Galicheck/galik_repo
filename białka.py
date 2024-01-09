import pandas as pd
import requests
from xml.dom.minidom import parseString, parse, Node


# df = pd.read_csv('proteins.csv')
# df['Id'] = df['Protein'].apply(lambda x: x.split('|')[1]).unique()
# df2 = df.query('Id != "iRT-Kit_WR_fusion" ').copy()



def get_protein_name(unique):
    response = requests.get('https://www.uniprot.org/uniprotkb/' + unique + '.xml')
    protein_data = response.text
    document = parseString(protein_data)
    # document.getElementsByTagName("fullName")
    fullName = document.getElementsByTagName("fullName")[0].firstChild.wholeText

    return fullName


# nazwy = []
# for i in uniques:
#     x = get_protein_name(i)
#     nazwy.append(x)
#
# print(nazwy)
#############################################
#zad3

from xml.sax import parse, SAXException
from xml.sax.handler import ContentHandler

class DictHandler(ContentHandler):


    def __init__(self):
        super().__init__()
        self.element_stack = []
    def startElement(self, name, attrs):
        """Run when opening tag is element"""
        self.element_stack.append({
            'name': name,
            'attributes': dict(attrs),
            'children': [],
            'value': ''
        })

        pass

    def endElement(self, name):
        if len(self.element_stack) > 1:
            child = self.element_stack.pop()
            self.current_element['children'].append(child)


    def characters(self, content):
        """Run when string is found"""
        self.current_element['value'] += content

    @property
    def current_element(self):
        return self.element_stack[-1]

class FullNameHandler(ContentHandler):
    def __init__(self):
        super().__init__()
        self.found_fullname = False
        self.fullname = " "

    def startElement(self, name, attrs):
        """Run when opening tag is element"""
        if name == 'fullName':
            self.found_fullname = True

    def endElement(self, name):
        if self.found_fullname:
            print("Value of fullName:", self.current_value)
            self.fullname = self.current_value
            # Interrupt parsing
            raise SAXException("Parsing interrupted after finding fullName")

    def characters(self, content):
        """Run when string is found"""
        self.current_value = content




'''
handler = DictHandler()
handler = FullNameHandler()
parse("./P01024.xml", handler)
root = handler.current_element
'''

filename = "./P01024.xml"

try:
    parse(filename, FullNameHandler())
except SAXException as e:
    if str(e) != "Parsing interrupted after finding fullName":
        # Handle other exceptions
        raise


