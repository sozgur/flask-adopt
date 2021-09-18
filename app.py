from flask import Flask, render_template, flash, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.debug = True
app.config['SECRET_KEY'] = "asSFYF235dsfgj$6f&dfsgsdhHJlgfd"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

db.create_all()

@app.route("/")
def list_pets():
    """List the pets"""
    pets = Pet.query.all()

    return render_template("list_pets.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Show form and add a pet in db"""

    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        flash(f"Created new pet")
        return redirect("/")
    else:
        return render_template("add_pet.html", form = form)


@app.route("/<int:pet_id>")
def show_pet(pet_id):
    """Show pet detail"""

    pet = Pet.query.get_or_404(pet_id)
 
    return render_template("detail.html", pet=pet)


@app.route("/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Show edit form and edit pet in db"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
  
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(f"/{pet_id}")
    else:
        return render_template("edit_pet.html", form=form)


























