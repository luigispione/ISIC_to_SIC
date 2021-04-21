import requests

from bs4 import BeautifulSoup

import re

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
    isicCode = isicCode.strip()
    r = requests.get("https://siccode.com/search-isic/" + isicCode)
    response = r.text
    return response

def search_isic_link(searchIsicPageResult: str) -> str:
    soup = BeautifulSoup(searchIsicPageResult, 'html.parser')
    isicLink = soup.find(href = re.compile("^https://siccode.com/isic-code/[0-9]*/.*"))
    hrefContent = isicLink.find("a")
    print(hrefContent)


isicCodes = retrieve_input_isic_codes()

for isicCode in isicCodes:
    response = search_isic_code(isicCode)
    search_isic_link(response)

