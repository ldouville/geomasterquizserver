from importlib import reload

from app import create_app, db
from app.models import User, Post, Country, Question
from scraping import scraper
from controller import Controller

app = create_app()
app.app_context().push()
controller = Controller()
countries = Country.query.all()
clist = countries[:4]

@app.shell_context_processor
def make_shell_context():
	return {
        'db': db,
        'scraper': scraper,
        'controller': controller,
        'User': User,
        'Post': Post,
        'Country': Country,
        'Question': Question,
        'clist': clist,
        'countries': countries,
        }