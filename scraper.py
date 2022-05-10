import requests
import urllib.request
import re
import time
from bs4 import BeautifulSoup


def get_citations_needed_count(url_string):
    response = requests.get(url_string)

    if response.status_code != 200:
        print("Error fetching page")
        exit()
    soup = BeautifulSoup(response.content, "html.parser")

    cits_needed = soup.findAll("a", string="citation needed")
    print(cits_needed)
    print(len(cits_needed))

    time.sleep(10)
    return len(cits_needed)

def get_citations_needed_report(url_string):
    response = requests.get(url_string)

    if response.status_code != 200:
        print("Error fetching page")
        exit()
    soup = BeautifulSoup(response.content, "html.parser")

    cits_needed = soup.findAll("p", "a", string="citation needed")
    print(cits_needed)
    print(len(cits_needed))

    time.sleep(10)


url = 'https://en.wikipedia.org/wiki/Gulf_of_Tonkin_incident'

# get_citations_needed_count(url)

get_citations_needed_report(url)