from flask import Blueprint, redirect, render_template, request,url_for
from .forms import CreatePostForm
from cozy_corner.models import User, Post
from flask_login import login_required
import requests as r
from cozy_corner import db

site = Blueprint('site', __name__, template_folder='site_templates')
current_user = User


@site.route('/library')
def library():

    return render_template('library.html', title = 'Browse Library')


@site.route('/cart')
def cart():

    return render_template('cart.html', title = 'Cart')


@site.route('/about')
@login_required
def signin():
    return render_template('about.html', title = 'About Me')


@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title = 'Profile')


@site.route('/wishlist')
@login_required
def wishlist():
    return render_template('wishlist.html', title = 'Wishlist')


@site.route('/read')
@login_required
def read():

    return render_template('read.html', title = 'Read')


@site.route('/readinglist')
@login_required
def readingList():
    return render_template('readinglist.html', title = 'Reading List')


@site.route('/userreviews')
@login_required
def userReviews():
    return render_template('userreviews.html', title = 'My Review')


@site.route('/bookinformation')
def bookInformation():

    return render_template('book.html', title = 'Book Summary')


@site.route('/post/create', methods= ["GET", "POST"])
@login_required
def createPost():
    form = CreatePostForm()
    if request.method == "POST":
        print('form was validated')
        title = form.title.data
        image= form.image.data
        content= form.content.data

        post = Post(title, image, content, current_user.id)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('site.profile'))
    return render_template('createpost.html', form = form)


@site.route('/search/book', methods= ["POST"])
def searchBook():
    if request.method == "POST":
        print ('request is made')
        book = request.form['book']
        data = data = r.get(f'https://www.goodreads.com/search/index.xml/{book}')
        if data.status_code == 200:
            my_data = data.json()

            book = {
                'title':"",
                'image':"",
                'genre':"",
                'author':""
            }
            for genre in my_data['genre']:
                book['genre'].append(genre['genre']['title'])
            book['title'] = my_data['title']
            book['image'] = my_data['image_url']
            book['author'] = my_data['author']

            title = book['title']
            image = book['image']
            genre = book['genre']
            author = book['author']

            book = book(title, image, genre, author)
            db.session.add(book)
            db.session.commit()
            return render_template('book.html', book = book)
        else:
            book=""
            return render_template('library.html', book = book)

