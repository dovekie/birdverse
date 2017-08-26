import os
from flask import (Flask, request, session, g, redirect, url_for, abort,
    render_template, flash)
from flask_sqlalchemy import SQLAlchemy
import import_birds
from taxon_levels import taxon_levels

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Bird

print('Running with {}'.format(os.environ['APP_SETTINGS']))

@app.route('/')
def default():
    return 'Welcome to Birdverse'

@app.route('/populate')
def populate_bird_data():
    stale_birds = db.session.query(Bird).delete()
    db.session.commit()
    print("Deleted {} stale birds".format(stale_birds))
    import_birds.populate_the_database()

    return 'This route fetches fresh bird data from outside source'

@app.route('/bird')
def bird_query():
    for key in request.args.keys():
        return get_a_bird(key, request.args[key])

def get_a_bird(taxon_level, bird):
    if taxon_level in taxon_levels:
        print('Valid taxon!')
    else:
        print('errr no.')
    return 'getting a bird: {} {}'.format(taxon_level, bird)

if __name__ == '__main__':
    app.run()