
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    firstname = db.Column(db.String(24), nullable=False)
    lastname = db.Column(db.String(24), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(4), nullable=False)
    firstname = db.Column(db.String(24), nullable=False)
    lastname = db.Column(db.String(24), nullable=False)
    middlename = db.Column(db.String(24), nullable=True)
    profession = db.Column(db.String(24), nullable=True)
    state = db.Column(db.String(24), nullable=True)
    room = db.relationship(
        'Room', backref='guest', uselist=False, lazy=True)

    def __repr__(self):
        return 'Guest: {}'.format(self.firstname)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    occupied = db.Column(db.Boolean, default=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=True)
    account = db.relationship(
        'Account', backref='room', uselist=False, lazy=True)

    def __repr__(self):
        return 'Room: {}'.format(self.number)


class Deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    account = db.relationship('Account', backref='deposit', lazy=True)

    def __repr__(self):
        return 'Deposit: {}'.format(self.amount)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.Boolean, default=False)
    total_dep = db.Column(db.Integer, nullable=True)
    deposit_id = db.Column(
        db.Integer, db.ForeignKey('deposit.id'), nullable=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=True)

    def __repr__(self):
        return '{}'.format(self.deposit)
