import re
import functools

import requests
from bs4 import BeautifulSoup

from scraping import fake_requests
from config import Config
from app.models import Country

class Scraper(object):

    def __init__(self):
       self.config = Config()

    def get_soup(self, url):
        response = requests.get(url)
        return BeautifulSoup(response.text, features="html.parser") # when using "real" requests, add .text to the response

    @property
    @functools.lru_cache()
    def all_country_endpoints(self):
        soup = self.get_soup(self.config.COUNTRY_LIST_URL)
        country_endpoints_list = []
        for table in soup.findAll("table", {"class", "wikitable alternance"}):
            for tr in table.findAll("tr")[1:]:
                a = tr.findAll("td")[1].a
                url = a["href"]
                country_endpoints_list.append(url)
        return country_endpoints_list

    def get_country_info_from_french(self, endpoint, logs=False):
        soup = self.get_soup(self.config.WIKI_URL + endpoint)
        title = self.clean_wiki_string(soup.find("h1", {"id": "firstHeading"}).string)
        infobox_div = soup.find("div", {"class": "infobox_v3"})
        
        for table in infobox_div.findAll("table"):
            if table.caption and (table.caption.string == "Administration"):
                administration_table = table
            if table.caption and (table.caption.string == "Géographie"):
                geography_table = table
            if table.caption and (table.caption.string == "Démographie"):
                demography_table = table
                
        # Administration
        for tr in administration_table.findAll("tr"):
            if tr.th.a and (tr.th.a.string == "Capitale"):
                # Delete parasiting coordinates
                if tr.td.p:
                    tr.td.p.decompose()
                capital = tr.td.a and tr.td.a.string or tr.td.text
                capital = self.clean_wiki_string(capital)
                break;
                
        # Géographie
        area = 0
        for tr in geography_table.findAll("tr"):
            if tr.th.string == "Superficie totale":
                area = self.clean_wiki_number(tr.td.text)
                break;
                
        # Démographie
        for tr in demography_table.findAll("tr"):
            if tr.th.a and (tr.th.a.string == "Population totale"):
                text =  tr.td.text
                population = self.clean_wiki_number(text)
                if "million" in text:
                    population = population*1000000
                break;

        if logs:
            print(f"{title}: {capital}, {area}, {population}")

        return Country(name=title, capital=capital, area=area, population=population)

    def clean_wiki_number(self, string):
        # Start at first number
        m = re.search(r"\d", string)
        string = string[m.start():]
        # Stop a first letter or a character of the list
        string = re.split("[a-zA-Z]|\[|\–|\,", string)[0]
        # Remove all space and cast to int
        return int(re.sub("\s", "", string))

    def clean_wiki_string(self, string):
        string = string.replace("\n", "")
        return re.split(" \(", string)[0]

    def scrap_french(self, start_index=0, logs=False):
        country_list = []
        for country_endpoint in self.all_country_endpoints[start_index:]:
            country_list.append(self.get_country_info_from_french(country_endpoint, logs=logs))
        return country_list

    def scrap_all(self, logs=False):
        country_dict = {}
        for country in self.scrap_french(logs=logs):
            country_dict[country.name] = country
        return country_dict