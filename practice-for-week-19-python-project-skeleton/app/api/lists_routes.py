from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import List

lists_routes = Blueprint('lists', __name__)


#get all lists by user
@lists_routes.route('/')
def lists_by_user():
  user = User.query.get(current_user.id)
  lists = List.query.filter(List.user_id == user.id).all()
  return jsonify(lists)

#get all lists by group
@lists_routes.route('/<int:group_id>')
def lists_by_group(group_id):
  lists = List.query.filter_by(group_id=group_id).all()
  return jsonify(lists)

#get all lists for day/ week/ month

#create new list
@lists_routes.route('/', methods=['POST'])
def create_lists():
  form = ListForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    data = form.data
    name = data['name']
    user_id = data['user_id']
    due = data['due']
    notes = data['notes']
    group_id = data['group_id']
    #res
  return jsonify('res')

#delete list by id
@lists_routes.route('/<int:list_id>')
def delete_list(list_id):
  list = List.query.get(list_id)
  tasks = Task.query.filter_by(list_id=list_id).all()
  if list:
    for task in tasks:
      db.session.delete(task)
      db.session.commit()
    db.session.delete(list)
    db.session.commit()
    return 'Successfully deleted list'
  return 'Could not delete list'

#update list by id
