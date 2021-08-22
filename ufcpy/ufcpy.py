import re
import math

import urllib.request

from bs4 import BeautifulSoup as bs

class UFCPyError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return repr(self.msg)

class Fighter(object):
    def __init__(self):
        self.base_url = "http://ufc.com/athlete"
        self.parsed_url = None
        self.name = None
        self.nick = None
        self.age = None
        self.record = None
        self.wins = None
        self.losses = None
        self.draws = None
        self.rank = None
        self.hometown = None
        self.active = None
        self.image_url = None
        self.height_inches = None
        self.striking_accuracy = None
        self.sig_strikes_landed = None
        self.sig_strikes_attempted = None
        self.grappling_accuracy = None
        self.landed_takedowns = None
        self.attempted_takedowns = None
        self.debut = None
        self.reach = None
        self.leg_reach = None
    
    def get_fighter(self, fighter):
        url = str(fighter).lower().replace(" ", "-")
        page = urllib.request.urlopen(f'{self.base_url}/{url}')
        self.parsed_url = bs(page, 'html.parser')
        self._get_attributes(fighter)

    def _get_attributes(self, fighter):
        self.name = self._parse_html('div', _class='c-hero--full__headline is-large-text').get_text().strip()
        self.age = self._parse_html('div', _class='field field--name-age field--type-integer field--label-hidden field__item').get_text()
        self.nick = self._parse_html('div', _class='field field-name-nickname').get_text().strip('/"')
        record = re.findall(r'\d+', self._parse_html('div', _class='c-hero__headline-suffix tz-change-inner').get_text().split('•')[1])
        self.record = f'{record[0]}-{record[1]}-{record[2]}'
        self.wins = record[0]
        self.losses = record[1]
        self.draws = record[2]
        self.hometown = self._parse_html('div', _class='c-bio__field c-bio__field--border-bottom-small-screens').get_text().replace('Hometown', '').strip()
        self.active = self._parse_html('div', _class="c-bio__text").get_text()
        self._weight_class()
        self._get_rank()
        self.image_url = self._parse_html('div', _class='c-bio__image--mobile').find_next().get('src')
        self.height_inches = self._parse_html('div', _class='c-bio__row--3col').get_text().split()[3].replace('.00', '')
        self._height_feet()
        self.striking_accuracy = self._parse_html('div', _class='l-overlap-group__item--odd').get_text().strip().split()[3]
        self.sig_strikes_landed = self._parse_html('div', _class='l-overlap-group__item--odd').get_text().strip().split()[8].replace('Landed', '')
        self.sig_strikes_attempted = self._parse_html('div', _class='l-overlap-group__item--odd').get_text().strip().split()[11].replace('Attempted', '')
        self.grappling_accuracy = self._parse_html('div', _class='l-overlap-group__item--even').get_text().strip().split()[3]
        self.landed_takedowns = self._parse_html('div', _class='l-overlap-group__item--even').get_text().strip().split()[7].replace('Landed', '')
        self.attempted_takedowns = self._parse_html('div', _class='l-overlap-group__item--even').get_text().strip().split()[9].replace('Attempted', '')
        second_stats = self._parse_html('div', _class='c-bio__row--3col', _find_all=True)[1].text.split()
        self.debut = f'{second_stats[2]} {second_stats[3]} {second_stats[4]}'
        self.reach = second_stats[6]
        self.leg_reach = second_stats[9]

    def _parse_html(self, _element, _id=None, _class=None, _find_all: bool = False):
        parsed = self.parsed_url.find(_element) or ""
        if _find_all == False:
            if _id is not None:
                parsed = self.parsed_url.body.find(_element, {'id': _id})
            if _class is not None:
                parsed = self.parsed_url.body.find(_element, {'class': _class})
            if _id is not None and _class is not None:
                parsed = self.parsed_url.body.find(_element, {'id': _id, 'class': _class})
        else:
            if _id is not None:
                parsed = self.parsed_url.body.find_all(_element, {'id': _id})
            if _class is not None:
                parsed = self.parsed_url.body.find_all(_element, {'class': _class})
            if _id is not None and _class is not None:
                parsed = self.parsed_url.body.find_all(_element, {'id': _id, 'class': _class})
        return parsed
    
    def _get_rank(self):
        rank = self._parse_html('div', _class='c-hero__headline-suffix tz-change-inner').get_text().split('•')[0].split('\n')
        if 'Champion' in rank[1]:
            self.rank = rank[1].strip()
        elif rank[1].strip().startswith('#'):
            self.rank = f'{rank[1].strip()} {rank[2].strip()}'
        else:
            self.rank = f'Unranked {rank[1].strip()} {rank[2].strip()}'

    def _weight_class(self):
        self.weight = self._parse_html('div', _class='c-bio__row--3col').get_text().split()[5].replace('.00', '')
        if self.weight == '125':
            self.weight_class = 'Flyweight'
        if self.weight == '135':
            self.weight_class = 'Bantamweight'
        if self.weight == '145':
            self.weight_class = 'Featherweight'
        if self.weight == '155':
            self.weight_class = 'Lightweight'
        if self.weight == '170':
            self.weight_class = 'Welterweight'
        if self.weight == '185':
            self.weight_class = 'Middleweight'
        if self.weight == '205':
            self.weight_class = 'Light Heavyweight'
        if self.weight == '250':
            self.weight_class = 'Heavyweight'

    def _height_feet(self):
        height_feet = round(int(self.height_inches) / 12, 1)
        new_height = str(height_feet).replace('.', ' ').split(' ')
        if new_height[1] == '0':
            self.height_feet = f'{new_height[0]} foot'
        else:
            self.height_feet = f'{new_height[0]} foot {new_height[1]} inch'