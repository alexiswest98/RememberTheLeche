from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Task

tasks_routes = Blueprint('tasks', __name__)


#get all tasks by user
def tasks():
  pass

#get all tasks by group
#get all tasks for day/ week/ month
#create new task
#delete task by id
#update task by id
