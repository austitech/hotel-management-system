from flask import Blueprint, redirect, url_for, render_template

from .forms import RoomForm, DepositForm
from .models import Room, Deposit, db


bp = Blueprint('room', __name__, url_prefix='/room')


@bp.route('/')
def list_room():
    rooms = Room.query.all()
    return render_template('room/list_room.html', rooms=rooms)


@bp.route('/add', methods=['GET', 'POST'])
def add_room():
    form = RoomForm()
    if form.validate_on_submit():
        room = Room(number=form.number.data)
        db.session.add(room)
        db.session.commit()
        return redirect(url_for('room.list_room'))

    return render_template('room/add_room.html', form=form)


@bp.route('/deposit', methods=['GET', 'POST'])
def deposit():
    form = DepositForm()
    occupied_rooms = Room.query.filter_by(occupied=True)
    occupied_rooms = [(room.number, room) for room in occupied_rooms]
    form.room.choices = occupied_rooms
    if form.validate_on_submit():
        room = Room.query.filter_by(number=form.room.data).first()
        dep = Deposit(
            amount=form.amount.data,
            account=[room.account]
        )
        total_dep = sum(dep.amount for dep in room.account.deposit.query.all())
        room.account.total_dep = total_dep
        db.session.add(dep)
        db.session.add(room)
        db.session.commit()

        return redirect(url_for('room.list_room'))
    return render_template('room/deposit.html', form=form)
