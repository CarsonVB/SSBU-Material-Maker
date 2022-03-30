import os
import json
from xml.dom import minidom
#Load shaders list from json into dictionary
with open('shaders.json', 'r') as f:
    shaders = json.load(f)

#User input for shader label and material name
label = ''
while not label.startswith('SFX_PBS_'):
    label = (input('Shader Label: '))
name = (input('Material Name: '))
params = shaders[label]

#Create XML document
root = minidom.Document()
xml = root.createElement('MaterialLibrary')
xml.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
xml.setAttribute('xmlns:xsd', 'http://www.w3.org/2001/XMLSchema')
root.appendChild(xml)
material1 = root.createElement('material')
material1.setAttribute('name', label)
material1.setAttribute('label', name)
xml.appendChild(material1)

#Add parameters to document
for j in params:
    print(j)
    filepath = os.path.join(r"params", j)
    print(filepath)
    custom = minidom.parse(filepath + '.xml')
    param1 = custom.getElementsByTagName('param')
    material1.appendChild(param1.item(0))
#Export XML document
xml_str = root.toprettyxml(indent='\t', encoding='utf-8')
print(xml_str)
with open('Material.xml', 'wb') as f:
    f.write(xml_str)
