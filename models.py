from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

IMG = "http://cdn.shopify.com/s/files/1/0164/2276/products/white_tiger_paw_Web_Decal-01_grande.png?v=1529583738"

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):

    __tablename__="pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Return default image if doesn't exist photo url in db"""
        
        return self.photo_url or IMG

