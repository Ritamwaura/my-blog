from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import Subscriber
from wtforms import ValidationError
