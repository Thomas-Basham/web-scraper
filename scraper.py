import requests
import time
from bs4 import BeautifulSoup


def get_citations_needed_count(url_string):
    response = requests.get(url_string)
    if response.status_code != 200:
        print("Error fetching page")
        exit()
    soup = BeautifulSoup(response.content, "html.parser")

    cits_needed = soup.findAll("span", string="citation needed")

    time.sleep(1)
    return len(cits_needed)


def get_citations_needed_report(url_string):
    response = requests.get(url_string)
    if response.status_code != 200:
        print("Error fetching page")
        exit()
    soup = BeautifulSoup(response.content, "html.parser")

    hearsay = soup.findAll("sup", class_="Template-Fact")

    unfounded_claims = ''

    for i in hearsay:
        unfounded_claims += (i.parent.text + '\n')

    time.sleep(1)
    return unfounded_claims


url = 'https://en.wikipedia.org/wiki/Gulf_of_Tonkin_incident'

print(get_citations_needed_count(url))
print(get_citations_needed_report(url))
