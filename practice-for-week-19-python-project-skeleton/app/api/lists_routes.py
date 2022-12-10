from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import List

user_routes = Blueprint('lists', __name__)


#get all lists by user
def lists():
  pass

#get all lists by group
#get all lists for day/ week/ month
#create new list
#delete list by id
#update list by id
