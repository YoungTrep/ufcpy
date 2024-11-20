from .utils import check_response

import requests
from bs4 import BeautifulSoup

def parse(url: str):
    res = requests.get(url)
    check_response(res)
    parsed_url = BeautifulSoup(res.content, "lxml")
    return parsed_url

def find_element(parsed_url: BeautifulSoup, element, id = None, clas = None, find_all: bool = False, *args, **kwargs):
    selectors = {}
    if id:
        selectors["id"] = id
    if clas:
        selectors["class"] = clas

    if find_all == True:
        parsed = parsed_url.find_all(element, selectors, *args, **kwargs)
    else:
        parsed = parsed_url.find(element, selectors, *args, **kwargs)
    return parsed