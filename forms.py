from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, validators
from wtforms.validators import InputRequired, Optional, Email

# class AddSnackForm(FlaskForm):
#     """Form for adding snacks."""

#     name = StringField("Snack Name")
#     price = FloatField("Price in USD")