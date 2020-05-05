
import os

from flask import Flask
from flask_migrate import Migrate

from .guest import bp as guest_bp
from .auth import bp as auth_bp
from .hotel import bp as hotel_bp
from .room import bp as room_bp

from .models import db, User
from .auth import login_manager

from .helpers import init_command


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # load instance config when not testing else load test config
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure instance dir exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # configure db and migration
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)
    init_command(app)

    # register view blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(hotel_bp)
    app.register_blueprint(room_bp)
    app.register_blueprint(guest_bp)

    return app
