from datetime import datetime
import random
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship("Post", backref="author", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Post {self.body}>"


q_c_association_table = db.Table('q_c_association_table',
    db.Column("question_id", db.Integer, db.ForeignKey("question.id"), primary_key=True),
    db.Column("country_id", db.Integer, db.ForeignKey("country.id"), primary_key=True)
)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    capital = db.Column(db.String(64), index=True)
    area = db.Column(db.Integer)
    population = db.Column(db.Integer)
    questions = db.relationship("Question", backref="right_answer", lazy="dynamic")

    def get_ordered_random_numbers(self, nb_max, forbidden_numbers, quantity=3):
        #TODO get this funciton out of the class to use is everywhere (if needed)
        if type(forbidden_numbers) is int:
            forbidden_numbers = [forbidden_numbers]
        random_numbers = []
        while len(random_numbers)  < quantity:
            x = random.randrange(1, nb_max + 1)
            if x not in forbidden_numbers + random_numbers:
                random_numbers.append(x)
        random_numbers.sort()
        return random_numbers

    def generate_questions(self, type, nb_of_questions):
        questions = []
        previous_questions = self.questions.all()
        all_countries = Country.query.all()
        id_max = max(c.id for c in all_countries)
        while len(questions) < nb_of_questions:
            random_numbers = self.get_ordered_random_numbers(id_max, self.id)
            answers = []
            for x in random_numbers:
                answer = next(c for c in all_countries if c.id == x)
                answers.append(answer)
            question = Question(type=type, right_answer=self, wrong_answers=answers)
            if question not in questions + previous_questions:
                questions.append(question)
        return questions
    
    def __repr__(self):
        return f"<Country {self.name}>"

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64), index=True)
    right_answer_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    wrong_answers = db.relationship("Country",
        secondary=q_c_association_table,
        lazy="subquery"
    )

    def __repr__(self):
        return f"<Question {self.type}: {self.right_answer.name}>"

    def __eq__(self, other):
        if not isinstance(other, Question):
            return NotImplemented
        return self.type == other.type and \
               self.right_answer == other.right_answer and \
               self.wrong_answers == other.wrong_answers


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
