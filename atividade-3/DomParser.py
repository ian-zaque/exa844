from xml.dom.minidom import parse
import time

BancoDocument = parse('map.osm')

print("Starting DOM Parser...")
start_time = time.time()
passedAmenity = False
id = ""
lat = 0.0
lon = 0.0
nome = ""
type = ""

for node in BancoDocument.getElementsByTagName("node"):
    id = node.getAttribute("id")
    lat = float(node.getAttribute("lat"))
    lon = float(node.getAttribute("lon"))
    
    for tag in node.getElementsByTagName("tag"):
        
        if tag.getAttribute("k") == "amenity":
            passedAmenity = True
            type = tag.getAttribute("v")
            
        if tag.getAttribute("k") == "name" and passedAmenity == True:
            nome = tag.getAttribute("v")
            passedAmenity = False
            print(f"ID: {id}, Nome: {nome}, Tipo: {type}, Lat.: {lat}, Lon.: {lon}")
            
end_time = time.time()
print("\n")
print("Tempo de Execução DomParser:", end_time - start_time, 'segundos')