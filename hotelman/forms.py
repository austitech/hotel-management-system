
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired


states = [
    ('Ab', 'Abia'), ('Im', 'Imo'), ('Rv', 'Rivers'),
    ('En', 'Enugu'), ('Eb', 'Ebonyi'), ('An', 'Anambra'),
]

title = [('mr', 'Mr'), ('mrs', 'Mrs'), ('miss', 'Miss')]


class LoginForm(FlaskForm):
    username = StringField('Username ', validators=[DataRequired(), ])
    password = StringField('Password ', validators=[DataRequired(), ])


class RegistrationForm(FlaskForm):
    username = StringField('Username ', validators=[DataRequired(), ])
    firstname = StringField('FirstName ', validators=[DataRequired(), ])
    lastname = StringField('LastName ', validators=[DataRequired(), ])
    email = StringField('Email Address ', validators=[DataRequired(), ])
    password = StringField('Password ', validators=[DataRequired(), ])


class RoomForm(FlaskForm):
    number = IntegerField('Room Number', validators=[DataRequired(), ])


class GuestRegistrationForm(FlaskForm):
    title = SelectField('Title', choices=title, validators=[DataRequired(), ])
    firstname = StringField('FirstName', validators=[DataRequired(), ])
    lastname = StringField('LastName', validators=[DataRequired(), ])
    middlename = StringField('MiddleName', validators=[])
    profession = StringField('Profession', validators=[])
    state = SelectField(
        'State', choices=states, validators=[])
    room = SelectField(
        'Room', coerce=int, validators=[DataRequired(), ])


class DepositForm(FlaskForm):
    amount = IntegerField('Amount', validators=[DataRequired(), ])
    room = SelectField(
        'Room', coerce=int, validators=[DataRequired(), ])
