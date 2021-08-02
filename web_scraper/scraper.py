import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Elektra_(character)"
page = requests.get(URL)
# print(page.content)


def get_citations_needed_count(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    citations_needed = soup.find_all(title="Wikipedia:Citing sources")
    return len(citations_needed)


def get_citations_needed_report(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    citations_needed = soup.find_all(title="Wikipedia:Citing sources")
    target_passages = [citation.find_parent("p").text for citation in citations_needed]
    passages_string = ""
    for passage in target_passages:
        passage = passage.strip("\n ")
        passages_string += passage + "\n\n- "

    return passages_string[:-2]


count = get_citations_needed_count(URL)
report = get_citations_needed_report(URL)
print(f"\nCitations Count: {count} ")
print(f"\n\nCitations Needed Report:\n\n- {report} ")
