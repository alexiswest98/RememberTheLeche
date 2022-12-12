from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from datetime import date
from app.models import Task, db
from app.forms.task_form import CreateTaskForm

tasks_routes = Blueprint('tasks', __name__, url_prefix="/api/tasks" )


#get all tasks by user
@tasks_routes.route('/all', methods=["GET"])
def get_all_tasks():
  tasks = Task.query.all()
  taskobject = [task.to_dict() for task in tasks]
  # print(task.name for task in tasks)
  return jsonify(taskobject)

#get all tasks by group NEED EVANS will be ''/api/groups/</int:id>/tasks'
# @tasks_routes.route('/lists/</int:id>', methods=["GET"])
# def get_list_tasks():

#   try:
#     listTasks = Task.query.filter(Task.list_id).all()
#   except LookupError:
#     raise ValueError("No tasks or lists found")

#   print(listTasks)
#   return 'listTasks'

#get all tasks for day/ week/ month
# @tasks_routes.route('/day', methods=["GET"])
# def get_day_tasks():
#   today = date.today()
#   # Textual month, day and year	
#   # d2 = today.strftime("%d/%m/%Y")
#   print(today)
#   # print("d2 =", d2)

#   # tasks = Task.query.filter(Task.due == d1).all()
#   tasks = Task.query.all()
#   print(task.due for task in tasks)
#   taskobject = [task.to_dict() for task in tasks]
#   return jsonify(taskobject)


# @tasks_routes.route('/week', methods=["GET"])
# def get_week_tasks():

# @tasks_routes.route('/month', methods=["GET"])
# def get_month_tasks():

# #create new simple task
@tasks_routes.route('/', methods=['POST'])
def create_task():
  form = CreateTaskForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  data = form.data

  if form.validate_on_submit():
    new_task = Task(
      name = data['name'],
      user_id = data['user_id'],
      list_id = data['list_id'],
      due = data['due'],
      notes = data['notes']
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict())
  return jsonify('You messed up', form.errors)
  

# #update task by id
@tasks_routes.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
  form = CreateTaskForm()
  task = Task.query.get(task_id)
  form['csrf_token'].data = request.cookies['csrf_token']
  data = form.data

  if task:
    task.name = data['name']
    task.user_id = data['user_id']
    task.due = data['due']
    task.notes = data['notes']
    task.completed_by = data['completed_by']
    db.session.commit()
    return (task.to_dict())
  return jsonify('could not find task')


# #delete task by id
@tasks_routes.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
  task = Task.query.get(task_id)
  if task:
    db.session.delete(task)
    db.session.commit()
    return 'Successfully deleted task'
  return 'Could not find task'
