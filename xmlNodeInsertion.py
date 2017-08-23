'''
Created on 14-Feb-2017

@author: BALASUBRAMANIAM
'''

import xml.etree.ElementTree as ET
tree = ET.parse('EmployeeData.xml')
root = tree.getroot()


#print(root)

for child in root:
   print (child.tag, child.attrib)
   
for emp in root.findall('Employee'):
    location = emp.find('Location').text
    mobileNo = emp.find('MobileNo').text
    print (location, mobileNo)
    


new = ET.Element('Employee')
root.insert(1, new)  # <-----------
print(ET.tostring(root))
for child in root:
   print (child.tag, child.attrib)
 
  
root = ET.fromstring(countrydata)

# Top-level elements
root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
root.findall("./country/neighbor")

# Nodes with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
root.findall(".//neighbor[2]")
'''