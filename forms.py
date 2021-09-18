from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, Length

class AddPetForm(FlaskForm):
    
    name = StringField("Pet Name", 
        validators=[InputRequired(message="Pet name can't be blank")])

    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])

    photo_url = StringField("Photo URL", 
        validators=[Optional(), URL(require_tld=True, message="Please enter valid URL")])

    age = IntegerField("Age", 
        validators=[Optional(), NumberRange(min=0, max=30, message="Age should be between 0 and 30")])

    notes = TextAreaField("Notes", 
        validators=[Optional(), Length(min=10)])



class EditPetForm(FlaskForm):

    photo_url = StringField("Photo URL", 
        validators=[Optional(), URL(require_tld=True, message="Please enter valid URL")])

    notes = TextAreaField("Notes", 
        validators=[Optional(), Length(min=10)])

    available = BooleanField("Available")