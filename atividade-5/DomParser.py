import urllib.request
from bs4 import BeautifulSoup

with open("seeds.txt") as f:
    links = f.readlines()

htmlStr = '<html> <head> <meta charset="UTF-8"> <title>EXA844 - Atividade 5</title> </head> <body> '
imgSection = ""

for link in links:
    page = urllib.request.urlopen(link)
    html = str(page.read().decode('utf-8'))

    soup = BeautifulSoup(html, 'html.parser')
    
    for img in soup.find_all('img'):
        imgSection = '<br> <h1>' + soup.title.string + '</h1> <img src=' + img.attrs.get("src") + ' alt=' + soup.title.string + '>'
        htmlStr = htmlStr + imgSection
        imgSection = '<p> ' + img.attrs.get("src") + '</p>'
        htmlStr = htmlStr + imgSection
    
htmlStr = htmlStr + ' </body> </html>'
reader = open('stringToHtml.html','w')
reader.write(htmlStr)
reader.close