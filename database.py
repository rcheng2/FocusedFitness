"""
Database for reviews
ref:
https://overiq.com/flask-101/authentication-in-flask/
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()

# pylint: disable=too-few-public-methods
class Comment(db.Model):
    """
    Database called Comment that contains infomation
    for the commenter's username, rating, and/or comment.
    """

    # pylint: disable=no-member
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    movieid = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(120))


class Users(db.Model, UserMixin):
    """
    Database called Comment that contains infomation
    for the commenter's username, rating, and/or comment.
    """

    # pylint: disable=no-member
    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)


class Record(db.Model):
    """ Table for exercise records """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    duration = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    exercise_type = db.Column(db.String())
    calories_burned = db.Column(db.String())


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

