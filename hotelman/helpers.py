import click
from werkzeug.security import generate_password_hash

from flask.cli import with_appcontext

from .models import User, db


def create_superuser():
    user = User(
        username='admin',
        firstname='Josiah',
        lastname='Augustine',
        email='austino@mymail.com',
        password=generate_password_hash('mypassword')
    )

    db.session.add(user)
    db.session.commit()


@click.command('create-superuser')
@with_appcontext
def create_superuser_command():
    """Create an admin user account."""
    try:
        create_superuser()
        click.echo('Admin user created successfully.')
    except Exception as e:
        click.echo(e)


def init_command(app):
    app.cli.add_command(create_superuser_command)
