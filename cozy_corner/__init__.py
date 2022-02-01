from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager()

from .models import User
from .site.routes import site
from .user_auth.routes import auth
# app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)
migrate = Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'user_auth.signin'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from cozy_corner import models