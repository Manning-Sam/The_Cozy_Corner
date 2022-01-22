from flask import Blueprint, redirect, render_template, request,url_for, session
from .forms import CarInfoForm
from cozy_corner.models import Car, db