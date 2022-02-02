from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, EqualTo, Email

class CreatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image Url')
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField()

class CreateReviewForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image Url')
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField()

class Search(FlaskForm):
    book = StringField("Search", validators= [DataRequired()])
    submit = SubmitField()

class AboutForm(FlaskForm):
    name = StringField('First, Last')
    bio = StringField('About Me')

class ReadingListForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image Url')
    genre = StringField('Genre', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])

class ReadListForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image Url')
    genre = StringField('Genre', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])

class WishlistForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image Url')
    genre = StringField('Genre', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])

class CartItem(FlaskForm):
    