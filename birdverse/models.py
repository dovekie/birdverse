from birdverse import db 
from sqlalchemy.dialects.postgresql import JSON

class Bird(db.Model):
    __tablename__ = 'birds'

    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String())
    species_name = db.Column(db.String())
    genus_name = db.Column(db.String())
    family_name = db.Column(db.String())
    order_name = db.Column(db.String())
    spuh = db.Column(db.String())

    def __init__(
        self, 
        common_name, 
        species_name, 
    	genus_name, 
    	family_name, 
    	order_name,
        spuh
    	):
        self.common_name = common_name
        self.species_name = species_name
        self.genus_name = genus_name
        self.family_name = family_name
        self.order_name = order_name
        self.spuh = spuh

    def __repr__(self):
        return ('<id {} common name {} species name {} genus name').format(
                self.id, 
                self.common_name, 
                self.species_name, 
                self.genus_name
                )

def connect_to_db(app):
    """Connect the database to our Flask app."""

    db.app = app
    db.init_app(app)