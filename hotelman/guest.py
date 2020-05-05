from flask import Blueprint, render_template, redirect, url_for

from .forms import GuestRegistrationForm
from .models import Guest, Room, Account, db


bp = Blueprint('guest', __name__, url_prefix='/guest')


@bp.route('/')
def list_guest():
    guests = Guest.query.all()
    return render_template('guest/list_guest.html', guests=guests)


@bp.route('/<id>')
def detail(id):
    guest = Guest.query.get(int(id))
    return render_template('guest/detail.html', guest=guest)


@bp.route('/checkin', methods=['GET', 'POST'])
def checkin():
    form = GuestRegistrationForm()
    occupied_rooms = Room.query.filter_by(occupied=False)
    occupied_rooms = [(room.number, room) for room in occupied_rooms]
    form.room.choices = occupied_rooms
    if form.validate_on_submit():
        guest = Guest(
            title=form.title.data,
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            middlename=form.middlename.data,
            profession=form.profession.data,
            state=form.state.data,
        )
        account = Account()
        room = Room.query.filter_by(number=form.room.data).first()
        room.account = account
        room.occupied = True
        guest.room = room
        db.session.add(guest)
        db.session.commit()
        return redirect(url_for('guest.list_guest'))
    return render_template('guest/checkin.html', form=form)
