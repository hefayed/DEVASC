import xml.etree.ElementTree as ET
with open('myfile.xml', 'r') as file:
  # converting an XML file to a python element tree
  mytree = ET.parse(file)

  # Get the root element of the tree
  myroot = mytree.getroot()

user = myroot.find('user')
print(user.find('name').text)

location = user.find('location')
print(location.find('city').text)

mylocation = location.findall('city')
for role in user.findall('roles'):
  print(role.text)

user.find('location').find('city').text = 'Dallas'
with open('myfile.xml', 'w') as file:
  mytree.write(file, encoding='unicode')