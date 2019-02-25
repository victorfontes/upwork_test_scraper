#/usr/bin/env python
#coding: utf-8

import requests
from bs4 import BeautifulSoup
import dateparser

TEST_URL = 'https://www.bestfightodds.com/events/ufc-231-holloway-vs-ortega-1584'
USER_AGENT = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36' }

def fetch_events_page_soup(url):
    res = requests.get(url, headers=USER_AGENT)
    soup = BeautifulSoup(res.content, 'lxml')
    return soup


def extract_event_details(soup):
    name = soup.select('div.table-header > a')[0].text
    date_human = soup.select('div > div.table-header > span')[0].text
    date = dateparser.parse(date_human).date()
    return {'name': name, 'date': date}


def extract_fights(soup):
    """Groups rows with fighter names in pairs, each pair is a fight."""
    fights = []

    for span in soup.select('table.odds-table-responsive-header > tbody > tr > th > a > span'):
        fighter_name = span.text
        
        if not len(fights) or len(fights[-1]) == 2:
            fights.append([fighter_name,])
            continue
        
        elif len(fights[-1]) == 1:
            fights[-1].append(fighter_name)
        
        else:
            raise ValueError('Number of fighter rows is not even.')
        
    return fights


def scrape_event_page(url):
    soup = fetch_events_page_soup(url)
    event = extract_event_details(soup)
    fights = extract_fights(soup)

    return fights


if __name__ == '__main__':
    print(scrape_event_page(TEST_URL))