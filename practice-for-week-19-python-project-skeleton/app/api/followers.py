from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User

follow_routes = Blueprint('follows', __name__)


#get all followers
def follow():
  pass
#unfollow
#
