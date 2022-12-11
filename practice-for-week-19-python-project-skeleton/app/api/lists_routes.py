from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import List, db, Task
from app.forms.list_form import ListForm

lists_routes = Blueprint('lists', __name__, url_prefix="/api/lists")


#get all lists by user
@lists_routes.route('/all', methods=['GET'])
def lists_by_user():
  # lists = List.query.filter(List.user_id == current_user.id).all()
  lists = List.query.all()
  list_obj = [list.to_dict() for list in lists]
  return jsonify(list_obj)

#get all lists by group #COME BY 
@lists_routes.route('/groups/<int:group_id>')
def lists_by_group(group_id):
  lists = List.query.filter(List.group_id == group_id).all()
  list_obj = [list.to_dict() for list in lists]
  return jsonify(list_obj)

#get all lists for day/ week/ month

#create new list
@lists_routes.route('/', methods=['POST'])
def create_lists():
  form = ListForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  data = form.data
  # print("********************", form.data)
  
  if form.validate_on_submit():
    new_list = List(
      name = data['name'],
      user_id = data['user_id'],
      due = data['due'],
      notes = data['notes'],
      group_id = data['group_id']
    )
    db.session.add(new_list)
    db.session.commit()
    return jsonify(new_list.to_dict())
  return jsonify('You messed up', form.errors)

#update list by id
@lists_routes.route('/<int:list_id>', methods=['PUT'])
def update_lists():
    form = ListForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
  
    if form.validate_on_submit():
      new_list = List(
        name = data['name'],
        user_id = data['user_id'],
        due = data['due'],
        notes = data['notes'],
        group_id = data['group_id']
      )
      db.session.add(new_list)
      db.session.commit()
      return jsonify(new_list.to_dict())
    return jsonify('You messed up', form.errors)

#delete list by id
@lists_routes.route('/<int:list_id>', methods=['DELETE'])
def delete_list(list_id):
  list = List.query.get(list_id)
  tasks = Task.query.filter(Task.list_id == list_id).all()
  if list:
    for task in tasks:
      db.session.delete(task)
      db.session.commit()
    db.session.delete(list)
    db.session.commit()
    return 'Successfully deleted list'
<<<<<<< HEAD
  return 'Could not find list'
=======
  return 'Could not find list'
>>>>>>> 01d6e897bc0f587b3e48bccc92c431a715fb8219
