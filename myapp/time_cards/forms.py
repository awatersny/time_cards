from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class TimeCardForm(FlaskForm):
  submit = SubmitField('Record Time Stamp')