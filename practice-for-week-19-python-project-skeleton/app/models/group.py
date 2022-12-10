from .db import db, environment, SCHEMA, add_prefix_for_prod




class Group(db.Model):
    __tablename__ = 'groups'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(100), default='https://moodlehub.ca/pluginfile.php/6842/mod_book/chapter/9131/group2.jpg')
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # Relationships
    group_to_task = db.relationship('Task', back_populates='task_to_group')
    group_to_list = db.relationship('List', back_populates='list_to_group')
    group_to_user = db.relationship('User', back_populates='user_who_created_group')