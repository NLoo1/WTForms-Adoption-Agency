from flask import Flask, flash, render_template, request, redirect
from forms import AddPetForm
from __init__ import create_app
from models import db, Pet

app = create_app()
db.app = app

@app.route("/")
def home():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route("/add", methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species=form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data
        new_pet = Pet(name=name,species=species,image_url=photo_url,age=age,notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f'{new_pet.name} added.')
        return redirect("/")
    else:
        return render_template('add-pet.html', form=form)

@app.route('/pets/<pet_id>')
def get_pet(pet_id):
    pet = Pet.query.get(pet_id)
    return render_template('pet.html', pet=pet)

@app.route('/pets/<pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species=form.species.data
        pet.photo_url=form.photo_url.data
        pet.age=form.age.data
        pet.notes=form.notes.data
        db.session.commit()
        flash(f'{pet.name} edited.')
        return redirect(f'/pets/{pet_id}')
    else:
        return render_template('add-pet.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
