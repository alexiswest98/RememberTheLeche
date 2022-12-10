from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User

user_routes = Blueprint('follows', __name__)


#get all followers
def follow():
  pass
#unfollow
#
