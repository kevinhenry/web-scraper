import requests
from bs4 import BeautifulSoup

# URL = "https://en.wikipedia.org/wiki/Jack_Russell_Terrier"
URL = "https://en.wikipedia.org/wiki/Elektra_(character)"
page = requests.get(URL)
# print(page.content)


def get_citations_needed_count(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    citations_needed = soup.find_all(title="Wikipedia:Citing sources")
    # citation_needed = soup.find_all("a", title="Wikipedia:Citation needed")
    # count = len(citations_needed)
    # print("Citations needed: ")
    # print(len(citations_needed))
    return len(citations_needed)


def get_citations_needed_report(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    # citations_needed = soup.find_all(title="Wikipedia:Citation needed")
    citations_needed = soup.find_all(title="Wikipedia:Citing sources")
    target_passages = [citation.find_parent("p").text for citation in citations_needed]
    passages_string = ""
    for passage in target_passages:
        passage = passage.strip("\n ")
        passages_string += passage + "\n\n- "

    #         # print("Passeages needing citation report: ")
    #         print(passages_string[:-2])
    return passages_string[:-2]


# print(get_citations_needed_count(URL))
# print(get_citations_needed_report(URL))

count = get_citations_needed_count(URL)
report = get_citations_needed_report(URL)

print(f"\nCitations Count: {count} \n\nCitations Needed Report:\n\n- {report} ")
