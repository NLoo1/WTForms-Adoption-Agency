import pdb
from unittest import TestCase
from flask import Flask
from app import app
from models import Pet, db
from flask_sqlalchemy import SQLAlchemy 
import os


with app.app_context():
    db.drop_all()   
    db.create_all()

class PetViewsTestCase(TestCase):
    def setUp(self):
        with app.app_context():
            db.create_all()
            Pet.query.delete()
            pet = Pet(name="Test",species="Cat")
            db.session.add(pet)
            db.session.commit()
            self.id= pet.id

    def tearDown(self):
        with app.app_context():
            db.drop_all()   
            db.session.rollback()
            db.session.commit()

    def test_list_pets(self):
        with app.app_context():
            with app.test_client() as client:
                # pdb.set_trace()
                resp = client.get("/", follow_redirects=True)
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn('Test', html)
                self.assertIn('Available', html)
                self.assertIn('Add new pet', html)
    
    def test_add_pet(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.get("/add", follow_redirects=True)
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn('Add pet', html)
                self.assertIn('Submit', html)
                self.assertIn('Back', html)

    def test_post_add_pet(self):
        with app.app_context():
            with app.test_client() as client:
                data = {
                    "name": "Test2",
                    "species": "Cat"
                }
                resp = client.post("/add", data=data, follow_redirects=True)
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn('Cat', html)

    def test_get_pet(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.get("/pets/1", follow_redirects=True)
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn('Test', html)
                self.assertIn('Cat', html)

    def test_edit_pet(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.get("/pets/1/edit", follow_redirects=True)
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn('Add pet', html)

    def test_post_edit_pet(self):
        with app.app_context():
            with app.test_client() as client:
                data = {
                    "name": "Test2",
                    "species": "Dog"
                }
                resp = client.post("/pets/1/edit", data=data, follow_redirects=True)
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn('Test2', html)
                self.assertIn('Dog', html)
