import xml.sax
import time

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.name = ""
    self.UID = ""
    self.lat = 0.0
    self.lon = 0.0
    self.type = ""
    self.passedAmenity = False

  def startElement(self, tag, attributes):
    if tag == "node":
      self.passedAmenity = False
      self.UID = attributes.get("id")
      self.lat = float(attributes.get("lat"))
      self.lon = float(attributes.get("lon"))
      
    if tag == "tag":
      if attributes.get("k") == "amenity":
        self.passedAmenity = True
        self.type = attributes.get("v")

      if attributes.get("k") == "name" and self.passedAmenity == True:
        self.name = attributes.get("v")
    
  def endElement(self, tag):
    if tag == "tag"  and self.isAllSet() and self.passedAmenity == True:
      print(f"ID: {self.UID}, Nome: {self.name}, Tipo: {self.type}, Lat.: {self.lat}, Lon.: {self.lon}")
      self.passedAmenity = False
      self.name = ""
      self.UID = ""
      self.lat = ""
      self.lon = ""
      self.type = ""

  def isAllSet(self):
    return not (self.name == "" or self.UID == "" or self.type == "" or self.lat == "" or self.lon == "")

start_time = time.time()

parser =  xml.sax.make_parser()
Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")

parser.parse("map.osm")
end_time = time.time()

print("\n")
print("Tempo de Execução SaxParser:", end_time - start_time, "segundos")