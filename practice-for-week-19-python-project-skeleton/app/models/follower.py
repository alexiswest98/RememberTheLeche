from .db import db, environment, SCHEMA, add_prefix_for_prod
# from .user import User


follows = db.Table(
    "follows",
    db.Column("follower_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("followed_id", db.Integer, db.ForeignKey("users.id"))
    )
