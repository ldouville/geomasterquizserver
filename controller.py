import random

from app import db
from app.models import Country
from scraping import scraper
import lib

class Controller(object):

    EXCLUDED_ATTR = ["_sa_instance_state", "id"]
    _new_country_list = []
    _differences = []

    def detect_updates(self, logs=False):
        diff_list = []
        previous_data = Country.query.all()
        new_data = scraper.scrap_all(logs=logs)
        for country in previous_data:
            new_country = new_data[country.name]
            diff_list.extend(self.compare_two_objects(country, new_country))
        if diff_list:
            self._differences = diff_list
            self._new_country_list = list(new_data.values())
        return diff_list

    def compare_two_objects(self, obj, ref):
        diffs = []
        for key in ref.__dict__:
            if key in self.EXCLUDED_ATTR:
                continue
            if getattr(obj, key) != getattr(ref, key):
                diffs.append(Diff(ref.name, key, getattr(obj, key), getattr(ref, key)))
        return diffs

    def apply_all_differences(self):
        if self._differences:
            country = Country.query.first()
            print("differences")
            for diff in self._differences:
                if diff.country != country.name:
                    country = Country.query.filter_by(name=diff.country).first()
                setattr(country, diff.attr, diff.value2)
            db.session.commit()
            self._differences = []
            self._new_country_list = []
        else:
            print("There is no differences to apply")

    def generate_new_questions(self, type, questions_per_country):
        for country in Country.query.all():
            for question in country.generate_questions(type, questions_per_country):
                db.session.add(question)
        db.session.commit()



class Diff(object):
    def __init__(self, country, attr, value1, value2):
        self.country = country
        self.attr = attr
        self.value1 = value1
        self.value2 = value2

    def __repr__(self):
        return f"<Diff on {self.country}:{self.attr}, {self.value1} <--> {self.value2}>"

