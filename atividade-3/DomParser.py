from xml.dom.minidom import parse

BancoDocument = parse('map.osm')

print("Starting DOM Parser...")
for c in BancoDocument.getElementsByTagName("node"):	
	# print("Nome:", c.getElementsByTagName("nome")[0].firstChild.data)
	# print("id: ", c.getAttribute("id"))
    for tag in c.getElementsByTagName("tag"):
        if tag.getAttribute("k") == "amenity":
            print("Tipo: ", tag.getAttribute("v"))
        
    # print("Nome: ", c.getElementsByTagName("tag"))
    # print("ID: ", self.UID) 
    # print("Tipo: ", self.type) 
    # print("Lat: ", self.lat)
    # print("Long: ", self.lon)