from .db import db, environment, SCHEMA, add_prefix_for_prod


class List(db.Model):
    __tablename__ = 'lists'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    due = db.Column(db.Date, nullable=False)
    notes = db.Column(db.String(1000))
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    list_to_group = db.relationship('Group', back_populates='group_to_list')
    list_to_task = db.relationship('Task', back_populates='task_to_list')
    list_to_user = db.relationship('User', back_populates='user_to_list')