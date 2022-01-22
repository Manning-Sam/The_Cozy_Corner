from flask import Blueprint, redirect, render_template, request,url_for,flash,session
from .forms import LoginForm, UserInfoForm
from cozy_corner.models import User, db
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user

auth = Blueprint('auth', __name__, template_folder = 'user_auth_templates')