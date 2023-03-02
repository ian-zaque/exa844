import xml.sax

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.name = ""
    self.UID = ""
    self.lat = ""
    self.lon = ""
    self.type = ""

  def startElement(self, tag, attributes):    
    if not self.isAllSet():
      if tag == "node":
        self.UID = attributes.get("id")
        self.lat = attributes.get("lat")
        self.lon = attributes.get("lon")
        
      if tag == "tag": 
        if attributes.get("k") == "amenity":
          self.type = attributes.get("v")

        if attributes.get("k") == "name":
          self.name = attributes.get("v")
    
  def endElement(self, tag):
    if tag == "tag" and self.isAllSet():
      print("Nome: ", self.name)
      print("ID: ", self.UID)
      print("Tipo: ", self.type) 
      print("Lat: ", self.lat)
      print("Long: ", self.lon)
      print("\n")

  def characters(self, content):
    if self.isAllSet():
      self.name = ""
      self.UID = ""
      self.lat = ""
      self.lon = ""
      self.type = ""

  def isAllSet(self):
    return self.name != "" and self.UID != "" and self.type != "" and self.lat != "" and self.lon != ""

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("map.osm")