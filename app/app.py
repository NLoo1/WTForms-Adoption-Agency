from flask import Flask, flash, render_template, request, redirect
from .forms import AddPetForm
from .__init__ import create_app
from .models import db, Pet

app = create_app()
db.app = app

if __name__ == '__main__':
    app.run(debug=True)
