import requests
from bs4 import BeautifulSoup

URL = "http://hak.hr"


def get_traffic_status():
    response = requests.get(URL)
    stranica = BeautifulSoup(response.content, "html.parser")
    return stranica.find("p", class_="content").get_text()
