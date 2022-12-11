from flask import Blueprint, jsonify, redirect
from flask_login import login_required
from datetime import date
from app.models import Task, db
from app.forms.task_form import 

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
@tasks_routes.route('', methods=['POST'])
def create_task():
  form = CreateTaskForm()
  # form['csrf_token'].data = request.cookies['csrf_token']

  if form.validate_on_submit():
    data = form.data
    new_task = Task(
      name = data['name'],
      user_id = data['user_id'],
      due = data['due'],
      notes = data['notes']
    )
    db.session.add(new_task)
    db.commit()
    return jsonify(new_task.to_dict())
  return "A problem occured"
  

# #create list task TEST WHEN GABES ARE DONE
# @tasks_routes.route('/lists/<int:id>/tasks', methods=['POST'])

# #update task by id
# @tasks_routes.route('/<int:id>', methods=['PUT'])

# #delete task by id
# @tasks_routes.route('/<int:id>', methods=['DELETE'])
