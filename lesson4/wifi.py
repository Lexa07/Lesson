import requests

# from flask import render_template

link = "http://192.168.0.1/"

resp = requests.get(link).text
#print(resp)

lol = open("zd4_1.py", "r", encoding="utf-8") #(r"link\file, "r", encoding="utf-8")
content = lol.read() #lol.readline()
print(content)
for i in lol:
    print(i, end="") #end убирает слеш н - /n перенос строки

lol.close()

with open....


 архив в материал

#1.1 или 2 способом
#2.
#3.


