import urllib.request
from bs4 import BeautifulSoup

with open("seeds.txt") as f:
    links = f.readlines()

htmlStr = '<html> <head> <meta charset="UTF-8"> <title>EXA844 - Atividade 5</title> </head> <body> '
imgSection = ""

for link in links:
    link = link.strip()
    page = urllib.request.urlopen(link)
    html = str(page.read().decode('utf-8'))

    soup = BeautifulSoup(html, 'html.parser')
    titulo = soup.title.string
    
    for img in soup.find_all('img'):
        src = img.attrs.get("src").strip()
        if "https://" not in src:
            if link[len(link)-1] == '/' or src[0] == '/':
                src =  link + src
            else:
                src = link + '/' + src
        src.strip()
        
        print("Titulo: ", titulo)
        print("Link: ", link)
        print("SRC: ", src, "\n")
        
        imgSection = '<br> <h1>' + titulo + '</h1> <img src=' + src + ' alt=' + titulo + ' width="500" height="300">'
        htmlStr = htmlStr + imgSection
        imgSection = '<p> ' + src + '</p>'
        htmlStr = htmlStr + imgSection
    
htmlStr = htmlStr + ' </body> </html>'
reader = open('stringToHtml.html','w')
reader.write(htmlStr)
reader.close