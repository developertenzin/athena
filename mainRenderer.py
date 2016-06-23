from lxml import etree

parser = etree.XMLParser(remove_comments=False)
tree = etree.parse('A-RrevisedtemplateFR76.4.L.xml', parser=parser)
# or alternatively set the parser as default:
# etree.set_default_parser(parser)



