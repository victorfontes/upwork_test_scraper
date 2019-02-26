#coding: utf-8
import requests
from bs4 import BeautifulSoup
import dateparser

from data import create_event, create_fighter, add_fight_to_event, get_abc_fighters, get_all_fights


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

from data import create_event, create_fighter, add_fight_to_event, get_abc_fighters, get_all_fights
def scrape_event_page(url):
    soup = fetch_events_page_soup(url)
    event = extract_event_details(soup)
    fights = extract_fights(soup)

    event_id = create_event(event['name'], event['date'])

    for fight in fights:
        fid_1 = create_fighter(fight[0])
        fid_2 = create_fighter(fight[1])
        add_fight_to_event(event_id, fid_1, fid_2)
    
    return event, fights    