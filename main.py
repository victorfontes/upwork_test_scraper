#/usr/bin/env python
#coding: utf-8

import requests
from bs4 import BeautifulSoup

TEST_URL = 'https://www.bestfightodds.com/events/ufc-231-holloway-vs-ortega-1584'
USER_AGENT = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36' }

def fetch_events_page(url):
    res = requests.get(url, headers=USER_AGENT)
    return res.content


def scrape_event_page(url):
    page_content = fetch_events_page(url)
    soup = BeautifulSoup(page_content)
    print(soup)


if __name__ == '__main__':
    print(scrape_event_page(TEST_URL))