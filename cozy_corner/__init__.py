from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import User,db,login_manager
from .user_auth.routes import user_auth
from .site.routes import site

app = Flask(__name__)

# app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(authentication)

app.config.from_object(Config)
migrate = Migrate(app,db)
db.init_app(app)

login_manager.init_app(app)
login_manager.login_view = 'authentication.signin'
