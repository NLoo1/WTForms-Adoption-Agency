import pdb
from unittest import TestCase
from app.__init__ import create_app
from app.models import Pet, db

app = create_app(config_class='config.TestConfig')
class PetViewsTestCase(TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        pet = Pet(name="Test", species="Cat")
        db.session.add(pet)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.session.rollback()
        db.drop_all()
        self.app_context.pop()

    def test_list_pets(self):
        with app.test_client() as client:
            resp = client.get("/", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Test', html)
            self.assertIn('Available', html)
            self.assertIn('Add new pet', html)
    
    def test_add_pet(self):
        with app.test_client() as client:
            resp = client.get("/add", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Add pet', html)
            self.assertIn('Submit', html)
            self.assertIn('Back', html)

    def test_post_add_pet(self):
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
        with app.test_client() as client:
            resp = client.get("/pets/1", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Test', html)
            self.assertIn('Cat', html)

    def test_edit_pet(self):
        with app.test_client() as client:
            resp = client.get("/pets/1/edit", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Add pet', html)

    def test_post_edit_pet(self):
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
