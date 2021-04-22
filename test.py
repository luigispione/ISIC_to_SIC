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
    r = requests.get("https://siccode.com/search-isic/" + isicCode, verify = False)
    response = r.text
    return response

def search_isic_link(searchIsicPageResult: str) -> str:
    soup = BeautifulSoup(searchIsicPageResult, 'html.parser')
    isicLink = str(soup.find(href = re.compile("^https://siccode.com/isic-code/[0-9]*/.*")))
    links = re.findall('".+?"', isicLink)
    nextLink = str(links[1])
    correctLink = nextLink[1:-1]
    return correctLink
    
isicCodes = retrieve_input_isic_codes()

for isicCode in isicCodes:
    isicCode = isicCode[0:4]
    response = search_isic_code(isicCode)
    completeLink = search_isic_link(response)
    r = requests.get(completeLink)
    isicResponse = r.text
    soup = BeautifulSoup(isicResponse, 'html.parser')
    isicLink = str(soup.find_all(href = re.compile("^https://siccode.com/sic-code/[0-9]*/.*")))
    smallLink = BeautifulSoup(isicLink, 'html.parser')
    sicList = []
    for span in smallLink.find_all('span'):
        sicList.append(span.text)
    d = dict()
    d[isicCode] = sicList
    print(d)
    #print(title.text)
    #span = smallLink.find_all('span')
    #print(span)
    
