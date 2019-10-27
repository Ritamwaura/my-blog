from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import Subscriber
from wtforms import ValidationError


class PostForm(FlaskForm):
    title = StringField("Post Title",validators=[Required()])
    post = TextAreaField("Write your post here")
    category = SelectField("Post Category",choices=[('Tech','Tech'),('Travel','Travel'),('Fashion','Fashion'),('Food','Food'),('Life','Life'),('Culture','Culture')],validators=[Required()])
    submit = SubmitField('Submit')
