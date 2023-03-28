from urllib.parse import parse_qs
import cgi, json, datetime

form = cgi.FieldStorage()
name = form["nome"].value
message = form["message"].value

file = open("./messages.json")
jsonFile = json.load(file)

obj = dict()
obj["name"] = name
obj["message"] = message
obj["created_at"] = f'{datetime.datetime.now()}'

jsonFile["messages"].append(obj)

jsonStr = json.dumps(jsonFile, indent=4, ensure_ascii=True)
jsonFile = open("./messages.json", "w")
jsonFile.write(jsonStr)
jsonFile.close()

file = open("./messages.json")
jsonFile = json.load(file)

print("Content-type: text/html;charset=utf-8")
print()
print("<html><head><title>Mensagens</title></head><body>")
for msg in jsonFile["messages"]:
    print("Nome: "+ msg["name"] + "<br>")
    print("Mensagem: "+ msg["message"] + "<br>")
    print("Horario: "+ msg["created_at"] + "<br>")
    print("<br>")
print("</body></html>")