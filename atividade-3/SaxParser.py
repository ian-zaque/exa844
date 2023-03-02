import xml.sax

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.name = ""
    self.UID = ""
    self.lat = ""
    self.lon = ""
    self.type = ""

  def startElement(self, tag, attributes):    
    self.name = ""
    self.lat = ""
    self.lon = ""
    self.type = ""
    
    if tag == "node":
      self.UID = attributes.get("id")
      self.lat = attributes.get("lat")
      self.lon = attributes.get("lon")
      
    if tag == "tag" and attributes.get("k") == "amenity":
        self.type = attributes.get("v")
    
    if tag == "tag" and attributes.get("k") == "name":
        self.name = attributes.get("v")

  def endElement(self, tag):
    if tag == "tag":
      print("Nome: ", self.name) 
      print("ID: ", self.UID) 
      print("Tipo: ", self.type) 
      print("Lat: ", self.lat)
      print("Long: ", self.lon)

  def characters(self, content):	
    self.name += content

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("Banco.xml")