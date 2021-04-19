import requests

r = requests.get("https://siccode.com/search-isic/0141")
response = r.text
responseFile = open("test.txt", 'w', encoding="utf-8")
responseFile.write(response)