from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, EqualTo, Email

class CreatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image Url')
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField()