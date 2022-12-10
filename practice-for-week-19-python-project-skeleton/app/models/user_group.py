from .db import db, environment, SCHEMA, add_prefix_for_prod
from .users import User
from .group import Group
from .user import User
from .group import Group

member = db.Table(
    'members',
    db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True, nullable=False )
)
