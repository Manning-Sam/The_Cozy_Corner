from datetime import datetime
from flask_login import UserMixin
from cozy_corner import db

# Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username= db.Column(db.String(150), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(150), nullable = False)
    post = db.relationship('Post', backref = 'author', lazy = True)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title= db.Column(db.String(150), nullable = True)
    image = db.Column(db.String(500), nullable = True)
    content = db.Column(db.String(450))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, title, image, content, user_id):
        self.title = title
        self.image = image
        self.content = content
        self.user_id = user_id


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title= db.Column(db.String(200), nullable = False)
    image = db.Column(db.String(500))
    genre = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(100), nullable = False)
    isbn = db.Column(db.String(200), nullable = False)
    price = db.Column(db.String(10), nullable = False)
    description = db. Column(db.String(1000), nullable = False)
        
    def __init__(self, title, image, genre, author, isbn, description, price):
        self.title = title
        self.image = image
        self.genre = genre
        self.author = author
        self.isbn = isbn
        self.price = price
        self.description = description
        
    def to_dict(self):
        return {
            'id': self.id,
            'title':self.title,
            'image':self.image,
            'genre':self.genre,
            'author':self.author,
            'price':self.price,
            'description': self.description,
        }


class UserReviews(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title= db.Column(db.String(200), nullable = False)
    image = db.Column(db.String(500))
    review = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('userid'), nullable = False)

    def __init__(self, title, image, review, user_id):
        self.title = title
        self.image = image
        self.review = review
        self.user_id = user_id

class ReadingList(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title= db.Column(db.String(200), nullable = False)
    image = db.Column(db.String(500))
    genre = db.Column(db.String(200), nullable = False)
    author = db.Column(db.String(200), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('userid'), nullable = False)

    def __init__(self, title, image, genre, author, user_id):
        self.title = title
        self.image = image
        self.genre = genre
        self.author = author
        self.user_id = user_id

class ReadList(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title= db.Column(db.String(200), nullable = False)
    image = db.Column(db.String(500))
    genre = db.Column(db.String(200), nullable = False)
    author = db.Column(db.String(200), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('userid'), nullable = False)

    def __init__(self, title, image, genre, author, user_id):
        self.title = title
        self.image = image
        self.genre = genre
        self.author = author
        self.user_id = user_id

class Wishist(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title= db.Column(db.String(200), nullable = False)
    image = db.Column(db.String(500))
    genre = db.Column(db.String(200), nullable = False)
    author = db.Column(db.String(200), nullable = False)
    price = db.Column(db.String(10), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('userid'), nullable = False)

    def __init__(self, title, image, genre, author, price, user_id):
        self.title = title
        self.image = image
        self.genre = genre
        self.author = author
        self.price = price
        self.user_id = user_id


# class CartItem(db.Model):
    __tablename__='cartitems'
    id = db.Column(db.Integer,primary_key=True)
    # adding the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# class BookItem(db.Model):
    __tablename__='Books in Cart'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64),unique=True)
    price = db.Column(db.Float,nullable=False)
    img = db.Column(db.String(64),unique=True)
    cartitems = db.relationship('CartItem', backref='Product')
    def __repr__(self):
        return '<ProductName %r>' % self.name