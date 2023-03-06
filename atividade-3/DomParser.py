from xml.dom.minidom import parse
import time

BancoDocument = parse('map.osm')

print("Starting DOM Parser...")
start_time = time.time()
passedAmenity = False

for element in BancoDocument.getElementsByTagName("node"):
    for tag in element.getElementsByTagName("tag"):
        
        if tag.getAttribute("k") == "amenity":
            passedAmenity = True
            print("\n")
            print("ID: ", element.getAttribute("id"))
            print("Lat: ", element.getAttribute("lat"))
            print("Long: ", element.getAttribute("lon"))
            print("Tipo: ", tag.getAttribute("v"))
            
        if tag.getAttribute("k") == "name" and passedAmenity == True:
            print("Nome: ", tag.getAttribute("v"))
            passedAmenity = False
            
end_time = time.time()
print("\n")
print("Tempo de Execução DomParser:", end_time - start_time, 'segundos')