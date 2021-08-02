Project Lab 17: Web Scraper

Deployed on: [Link](https://github.com/kevinhenry/web-scraper)

PR: [Link](https://github.com/kevinhenry/web-scraper/pulls)

Collaboration:
  Tony Regalado, Anthony Williams

Overview: A key developer skill is the ability to use internet resources effectively. Especially when learning a new topic.

For this lab you’ll be converting an excellent tutorial from a couple years ago. Does it still work? Let’s find out!

NOTE: you don’t have to understand all of the code in the tutorial yet. Get it working first, in the process it will become more familiar.

## Feature Tasks and Requirements
[x] Scrape a Wikipedia page and record which passages need citations.
[x] E.g. History of Mexico has 7 “citation needed” cases, as of this writing.
[x] Your web scraper should report the number of citations needed.
[x] Your web scraper should identify those cases AND include the relevant passage.
[x] E.g. Citation needed for “lorem spam and impsum eggs”
[x] Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.


## Implementation Notes
[x] Count function must be named get_citations_needed_count
[x] get_citations_needed_report takes in a url and returns a string
[x] Report function must be named get_citations_needed_report
[x] get_citations_needed_report takes in a url and returns a string
[x] the string should be formatted with each citation needed on own line, in order found.
[x] Module must be named scraper.py

### User Acceptance Tests:
[x] verify that correct count of citations needed is calculated
[x] verify that preceding passage

Tools Used
request
BeautifulSoup


Python
Pytest
Poetry
PyEnv

Getting Started
Clone this repository to your local machine.

$ git clone [Link](https://github.com/kevinhenry/web-scraper.git)
Once downloaded, activate your virtual environment and run by ____________

`poetry init`
`poetry shell`
