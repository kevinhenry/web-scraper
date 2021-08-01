from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report


def test_citation_count():
    actual = get_citations_needed_count("https://en.wikipedia.org/wiki/Elektra_(character)")
    expected = 15
    assert actual == expected


def test_citation_report():
    URL = "https://en.wikipedia.org/wiki/Elektra_(character)"
    actual = get_citations_needed_report(URL)
    assert type(actual) == str
