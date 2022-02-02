from flask import Blueprint, redirect, render_template, request,url_for
from .forms import CreatePostForm, Search, CreateReviewForm
from cozy_corner.models import User, Post
from flask_login import login_required
import requests as r
from cozy_corner import db

site = Blueprint('site', __name__, template_folder='site_templates')
current_user = User


@site.route('/', methods=["GET"])
def library():
#   if request.method == "GET":
    
    return render_template('library.html', title = 'Browse Library')


@site.route('/cart', methods=["GET","POST"])
def cart():
    # if request.method == "GET":
    # if request.method == "POST":
    return render_template('cart.html', title = 'Cart')


@site.route('/about', methods=["GET","POST"])
@login_required
def about():
    # if request.method == "GET":
    # if request.method == "POST":
    return render_template('about.html', title = 'About Me')


@site.route('/profile', methods=["GET","POST"])
@login_required
def profile():
    # if request.method == "GET":
    # if request.method == "POST":
    return render_template('profile.html', title = 'Profile')


@site.route('/wishlist', methods=["GET","POST"])
@login_required
def wishlist():
    # if request.method == "GET":
    # if request.method == "POST":
    return render_template('wishlist.html', title = 'Wishlist')


@site.route('/readlist', methods=["GET","POST"])
@login_required
def read():
    # if request.method == "GET":
    # if request.method == "POST":
    return render_template('read.html', title = 'Read')


@site.route('/readinglist', methods=["GET","POST"])
@login_required
def readingList():
    # reading_list_form = 
    # if request.method == "GET":
        print ('request is made')
        reading_list = reading_list_form.book.data
        print(reading_list)
        data = data = r.get(f'')
        if data.status_code == 200:
            my_data = data.json()

            reading_list = {
                'book':{
                    'title':"",
                    'image':"",
                    'genre':"",
                    'author':"",
                }
            }
            for genre in my_data['genre']:
                reading_list['book']['genre'].append(genre['genre']['title'])
            reading_list['book']['title'] = my_data['title']
            reading_list['book']['image'] = my_data['image_url']
            reading_list['book']['author'] = my_data['author']

            title = reading_list['book']['title']
            image = reading_list['book']['image']
            genre = reading_list['book']['genre']
            author = reading_list['book']['author']
            

            list = reading_list['book'](title, image, genre, author)
            db.session.add(list)
            db.session.commit()
            return render_template('readinglist.html', form = reading_list_form)
        else:
            book=""
            return render_template('base.html', form = reading_list_form)

        # if request.method == "POST":

    return render_template('readinglist.html', title = 'Reading List')


@site.route('/userreviews', methods=["GET","POST"])
@login_required
def userReviews():
    # if request.method == "GET":
    # if request.method == "POST":
    review_form = CreateReviewForm()

    return render_template('userreviews.html', title = 'My Review')


@site.route('/bookinformation', methods=["GET","POST"])
def bookInformation():
    search_form = Search()
    if search_form.validate_on_submit():
        print ('request is made')
        book = search_form.book.data
        print(book)
        data = data = r.get(f'https://www.goodreads.com/search/index.xml/{book}')
        if data.status_code == 200:
            my_data = data.json()

            book = {
                'title':"",
                'image':"",
                'genre':"",
                'author':"",
                'description':"",
                'reviews':{'':""}
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
            description = book['description']
            reviews = book['reviews']

            book = book(title, image, genre, author, description, reviews)
            db.session.add(book)
            db.session.commit()
            return render_template('book.html', form = search_form)
        else:
            book=""
            return render_template('base.html', form = search_form)

    return render_template('book.html', title = 'Book Summary')


@site.route('/suggestions')
def suggestions():

    return render_template('suggesetions.html', title = 'Suggestions')


@site.route('/post/create', methods= ["GET", "POST"])
@login_required
def createPost():
    post_form = CreatePostForm()
    if request.method == "POST":
        print('form was validated')
        title = post_form.title.data
        image= post_form.image.data
        content= post_form.content.data

        post = Post(title, image, content, current_user.id)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('site.profile'))
    return render_template('createpost.html', form = post_form)


@site.route('/search/book', methods= ["POST","GET"])
def searchBook():
    search_form = Search()
    if search_form.validate_on_submit():
        print ('request is made')
        book = search_form.book.data
        print(book)
        data = data = r.get(f'https://www.goodreads.com/search/index.xml/{book}')
        if data.status_code == 200:
            my_data = data.json()

            book = {
                'title':"",
                'image':"",
                'genre':"",
                'author':"",
                'description':"",
                'reviews':{'':""}
            }
            for genre in my_data['genre']:
                book['genre'].append(genre['genre']['title'])
            book['title'] = my_data['title']
            book['image'] = my_data['image_url']
            book['author'] = my_data['author']
            book['description'] = my_data['description']
            book['reviews'] = my_data['reviews']

            title = book['title']
            image = book['image']
            genre = book['genre']
            author = book['author']
            description = book['description']
            reviews = book['reviews']

            book = book(title, image, genre, author, description, reviews)
            db.session.add(book)
            db.session.commit()
            return render_template('book.html', form = search_form)
        else:
            book=""
            return render_template('base.html', form = search_form)


@app.route('/cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):

    product = Product.query.filter(Product.id == product_id)
    cart_item = CartItem(product=product)
    db.session.add(cart_item)
    db.session.commit()

    return render_tempate('home.html', product=products)