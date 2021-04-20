import requests

#r = requests.get("https://siccode.com/search-isic/0141")
#response = r.text
#responseFile = open("test.txt", 'w', encoding="utf-8")
#responseFile.write(response)

def retrieve_input_isic_codes() -> list: 
    inputFile = open("Input.csv", 'r')
    lines = inputFile.readlines()
    isicCodes = []
    for line in lines:
        lineArray = line.split(";")
        isicCode = lineArray[3]
        isicCodes.append(isicCode)
    return isicCodes 

def search_isic_code(isicCode: str) -> str:
    params = {"isicCode" : isicCode}
    r = requests.get("https://siccode.com/search-isic", params = params)
    response = r.text
    return response

isicCodes = retrieve_input_isic_codes()

for isicCode in isicCodes:
    response = search_isic_code(isicCode) 
    print(response)

