from xml.dom.minidom import parse
import json
import time

BancoDocument = parse('map.osm')

print("Starting DOM Parser...")
start_time = time.time()
passedAmenity = False

jsonMap = dict()
jsonMap["type"] = "FeatureCollection"
jsonMap["features"] = []
features = []

location = dict()
location["type"] = "Feature"
location["geometry"] = dict()
location["geometry"]["type"] = "Point"
location["geometry"]["coordinates"] = []
location["properties"] = dict()
location["properties"]["nome"] = ""
location["properties"]["tipo"] = ""

for node in BancoDocument.getElementsByTagName("node"):
    location["geometry"]["coordinates"] = [float(node.getAttribute("lon")), float(node.getAttribute("lat"))]
    
    for tag in node.getElementsByTagName("tag"):
        if tag.getAttribute("k") == "amenity":
            passedAmenity = True
            location["properties"]["tipo"] = tag.getAttribute("v")
            
        if tag.getAttribute("k") == "name" and passedAmenity == True:
            location["properties"]["nome"] = tag.getAttribute("v")

        if location["properties"]["nome"] != "" and passedAmenity == True:
            passedAmenity = False
            features.append(location)

    location = dict()
    location["type"] = "Feature"
    location["geometry"] = dict()
    location["geometry"]["type"] = "Point"
    location["geometry"]["coordinates"] = []
    location["properties"] = dict()
    location["properties"]["nome"] = ""
    location["properties"]["tipo"] = ""
    
jsonMap["features"] = features

jsonStr = json.dumps(jsonMap, indent=4, ensure_ascii=True)
jsonFile = open("map.json", "w")
jsonFile.write(jsonStr)
jsonFile.close()

end_time = time.time()
print("Tempo de Execução DomParser:", end_time - start_time, 'segundos')