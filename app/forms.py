from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, FloatField, TextAreaField, validators
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name= StringField("Pet Name",
                      validators=[InputRequired()])
    species= SelectField("Species",
                      validators=[InputRequired()], choices=[('Dog','Dog'),('Cat','Cat'),('Porcupine','Porcupine')])
    photo_url= StringField("Photo URL",
                      validators=[Optional()])
    age= IntegerField("Age",
                      validators=[Optional()])
    notes= TextAreaField("Notes",
                      validators=[Optional()])
