from .db import db, environment, SCHEMA, add_prefix_for_prod

class Task(db.Model):
    __tablename__ = 'tasks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    #this boolean helps us count how many a user has completed
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    due = db.Column(db.Date, nullable=False)
    notes = db.Column(db.String(1000))
    completed_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # Relationships
    task_to_user = db.Relationship('User', back_populates='user_to_task')
    task_to_list = db.relationship('List', back_populates='list_to_task')
    task_creator = db.relationship('User', back_populates='user_who_created_task')
    task_to_group = db.relationship('Group', back_populates='group_to_task')
