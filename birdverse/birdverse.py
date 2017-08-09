import os
from flask import (Flask, request, session, g, redirect, url_for, abort,
    render_template, flash)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Bird

print 'Running with {}'.format(os.environ['APP_SETTINGS'])

@app.route('/')
@app.route('/<bird>')
def default(bird=None):
    if bird:
        return get_a_bird(bird)
    return 'Welcome to Birdverse'

@app.route('/populate')
def populate_bird_data():
    return 'This route will fetch fresh bird data from outside source'


def get_a_bird(bird):
    return 'getting a bird: {}'.format(bird)

if __name__ == '__main__':
    app.run()