from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import User, Group, db
from ..forms.group_form import GroupForm
groups_routes = Blueprint('groups', __name__)

#get all groups
@groups_routes.route('')
# @login_required
def get_groups():
  groups = Group.query.all()
  return jsonify([group.to_dict() for group in groups])


@groups_routes.route('/<int:id>', methods=['DELETE'])
# @login_required
def delete_group(id):
    group = Group.query.get(id)
    db.session.delete(group)
    db.session.commit()
    return "Group successfully deleted"


@groups_routes.route('/create', methods=['POST'])
# @login_required
def create_group():
  form = GroupForm()
  if form.validate_on_submit():
    group = Group(
    name = form.data['name'],
    image_url= form.data['image_url']
    )
    db.add(group)
    db.commit()
    return 'jsonify(group)'

  if form.errors:
    return('Bad Data')