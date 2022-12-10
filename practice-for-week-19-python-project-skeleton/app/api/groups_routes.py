from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User

groups_routes = Blueprint('groups', __name__)


#get all followers
def group():
  pass
#unfollow
#follow someone