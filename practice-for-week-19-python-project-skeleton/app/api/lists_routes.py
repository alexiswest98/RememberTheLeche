from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import List

user_routes = Blueprint('lists', __name__)

def lists():
  pass
