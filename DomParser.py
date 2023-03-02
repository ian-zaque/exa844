from xml.dom.minidom import parse

BancoDocument = parse('map.osm')

print("Starting DOM Parser...")
for element in BancoDocument.getElementsByTagName("node"):
    for tag in element.getElementsByTagName("tag"):
        
        if tag.getAttribute("k") == "amenity":
            print("ID: ", element.getAttribute("id"))
            print("Lat: ", element.getAttribute("lat"))
            print("Long: ", element.getAttribute("lon"))
            print("Tipo: ", tag.getAttribute("v"))
            
        if tag.getAttribute("k") == "name":
            print("Nome: ", tag.getAttribute("v"))