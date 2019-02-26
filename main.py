#!/usr/bin/env python
#coding: utf-8

import click
from scraper import scrape_event_page
from data import get_abc_fighters, get_all_fights

TEST_URL = 'https://www.bestfightodds.com/events/ufc-231-holloway-vs-ortega-1584'


@click.group()
def cli():
    pass


@cli.command('scrape-event', help='Scrape and persist data from ufc event page.')
def scrape_event():
    event, fights = scrape_event_page(TEST_URL)
    click.secho('Event: {name} on {date}'.format(**event), bold=True)
    click.secho('%d fights imported.' % len(fights))


@cli.command('show-abc-fighters', help='Display fighters with name starting with A,B or C.')
def show_abc_fighters():
    rows = get_abc_fighters()
    click.echo(rows.dataset)


@cli.command('show-fights', help='Display all fights from all events.')
def show_fights():
    rows = get_all_fights()
    click.echo(rows.dataset)








if __name__ == '__main__':
    cli()
