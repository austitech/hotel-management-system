from flask import Blueprint, render_template

from .forms import LoginForm

bp = Blueprint('hotel', __name__)

@bp.route('/', methods=['GET'])
@bp.route('/home', methods=['GET'])
def home():
    form = LoginForm()
    return render_template('hotel/home.html', form=form)
