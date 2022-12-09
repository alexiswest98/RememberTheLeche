def ignore():
    pass

from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

# join table for members
member = db.Table(
    'members',
    db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True, nullable=False )
)

# Join table for followers
follows = db.Table(
    "follows", 
    db.Column("follower_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("followed_id", db.Integer, db.ForeignKey("users.id"))
)

class List(db.Model):
    __tablename__ = 'lists'
    
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

class Task(db.Model):
    __tablename__ = 'tasks'
    
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



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # Relationships
    user_to_task = db.relationship('Task', back_populates='task_to_user')
    user_who_created_task = db.relationship('Task', back_populates='task_creator')
    user_who_created_group = db.relationship('Group', back_populates='group_to_user')
    user_to_list = db.relationship('List', back_populates='list_to_user')

    followers = db.relationship(
        "User", 
        secondary=follows,
        primaryjoin=(follows.c.follower_id == id),
        secondaryjoin=(follows.c.followed_id == id),
        backref=db.backref("following", lazy="dynamic"),
        lazy="dynamic"
        )


class Group(db.Model):
    __tablename__ = 'groups'

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
