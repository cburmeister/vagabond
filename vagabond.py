#! /usr/bin/env python

import json
import click
import requests
from bs4 import BeautifulSoup
from werkzeug.urls import url_quote_plus
from collections import OrderedDict


@click.command()
@click.option('--query', default='', help='Where do you want to go.')
@click.option('--checkin', default='', help='Date of arrival.')
@click.option('--checkout', default='', help='Date of departure.')
@click.option('--guests', default='', help='Number of guests.')
def main(query, checkin, checkout, guests):
    """
    Search https://www.airbnb.com/ without leaving the prompt.
    """
    args = {
        'checkin': checkin,
        'checkout': checkout,
        'guests': guests,
    }
    params = '&'.join([
        '%s=%s' % (k, url_quote_plus(v)) for k, v in args.items()
    ])
    url = '%s?%s' % ('https://www.airbnb.com/s/%s' % query, params)

    r = requests.get(url)
    soup = BeautifulSoup(r.content)

    listings = []

    for div in soup.find_all('div', {'class': 'listing'}):
        price_span = div.find('span', {'class': 'price-amount'})
        summary_div = div.find('div', {'class': 'listing-location'})
        instant_span = div.find('span', {'class': 'h3 icon-beach'})

        listing = OrderedDict([
            ('url', div.attrs.get('data-url')),
            ('price', float(price_span.text)),
            ('name', div.attrs.get('data-name')),
            ('instant', bool(instant_span)),
            ('lat', div.attrs.get('data-lat')),
            ('lng', div.attrs.get('data-lng')),
            ('summary', summary_div.text),
        ])
        listings.append(listing)

    listings = sorted(listings, key=lambda k: k['price']) 

    click.echo(json.dumps(listings, indent=4, sort_keys=True))



if __name__ == "__main__":
   main()
