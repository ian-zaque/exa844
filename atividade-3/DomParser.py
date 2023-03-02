from xml.dom.minidom import parse

BancoDocument = parse('Banco.xml')

print("Starting DOM Parser...")
for c in BancoDocument.getElementsByTagName("Cliente"):	
	print("Nome:", c.getElementsByTagName("nome")[0].firstChild.data)
	print("id: ", c.getAttribute("id"))