"""Seed file to make sample data for db."""

from app.models import Pet
from app.app import app, db

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

    # name, species, available REQUIRED
    pet1 = Pet(name="Rocky", species="Hamster", available=True)
    pet2 = Pet(name="Comet", species="Goldfish", available=True)
    pet3 = Pet(name="Nova", species="Cat", available=True)

    db.session.add_all([pet1,pet2,pet3])
    db.session.commit()
