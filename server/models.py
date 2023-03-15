from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.Integer)

    @validates('name')
    def validate_name(self, key, name):
        if name == '':
            raise ValueError("Must have a name")
        return name

    @validates('phone_number')
    def validate_phone(self, key, number):
        if len(number) != 10:
            raise ValueError("Phone number muse bt exactly 10 digits long")
        return number


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    summary = db.Column(db.String)
    category = db.Column(db.String)

    @validates('title')
    def validate_name(self, key, title):
        if title == '':
            raise ValueError("Must have a title")
        if not any(each in title for each in ["Won't Believe", "Secret", "Top", "Guess"]):
            raise ValueError("Needs clickbait")
        return title

    @validates('content')
    def validate_content(self, key, content):
        if len(content) <= 250:
            raise ValueError("Must be longer than 250 characters")
        return content
    
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("Must be shorter than 250 characters")
        return summary

    @validates('category')
    def validate_category(self, key, category):
        if category != "Fiction" and category != "Non-Fiction":
            raise ValueError("Must be Fiction or Non-Fiction")
        return category