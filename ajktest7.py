import os


# Change the directory, so Excel file is in the current working directory.
os.getcwd()
print("Original path is:  " + os.getcwd())
path = "./"
os.chdir(path)
print("Current path is:")
print(os.getcwd())


import xml.etree.ElementTree as ET

with open('A-RrevisedtemplateFR76.4.L.xml', encoding="utf8") as f:
  tree = ET.parse(f)
  root = tree.getroot()

  for elem in root.getiterator():
    print(elem)
  '''
  for elem in root.getiterator():
    try:
      elem.text = elem.text.replace('FEATURE NAME', 'THIS WORKED')
      elem.text = elem.text.replace('FEATURE NUMBER', '123456')
    except AttributeError:
      pass
  '''



tree.write('newfile.xml', encoding="utf8")
