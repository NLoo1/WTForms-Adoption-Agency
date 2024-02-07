from flask import Flask, render_template, request, redirect
from .__init__ import create_app
from .models import db, Pet

app = create_app()
db.app = app

@app.route("/")
def home():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

if __name__ == '__main__':
    app.run(debug=True)
