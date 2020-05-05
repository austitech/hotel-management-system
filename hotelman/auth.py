from werkzeug import check_password_hash, generate_password_hash

from flask import (Blueprint, redirect, render_template, request,
                  flash, url_for)
from flask_login import LoginManager, login_user, logout_user

from .forms import LoginForm, RegistrationForm
from .models import User, db


bp = Blueprint('auth', __name__, url_prefix='/auth')
login_manager = LoginManager()


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("Logged-in Successfully")
                redirect(url_for('hotel.home'))
            else:
                flash("Invalid login credentials")
    return redirect(url_for('hotel.home', form=form))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(
                username=form.username.data,
                firstname=form.firstname.data,
                lastname=form.lastname.data,
                email=form.email.data,
                password=generate_password_hash(form.password.data)
            )
            db.session.add(user)
            db.session.commit()
            flash("Registration Successful")
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('hotel.home'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
