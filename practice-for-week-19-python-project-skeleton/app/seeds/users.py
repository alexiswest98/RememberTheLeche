from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password')
    alexis_west = User( username='Alexis West', password='password123', email='alexis@gmail.com', image_url='', )
    michael_lacey = User( username='Michael Lacey', password='password123', email='michael@gmail.com', image_url='', )
    gabriel_day = User( username='Gabriel Day', password='password123', email='gabester1@gmail.com', image_url='', )
    evan_morgan = User( username='Evan Morgan', password='password123', email='captainmorgan@gmail.com', image_url='', )
    seed_user = User( username='Jared Couglhing', password='password123', email='jaredc@gmail.com', image_url='', )
    seed_user1 = User( username='David Bonkano', password='password123', email='DavidBonk@gmail.com', image_url='', )
    seed_user2 = User( username='Jennifer Wyling', password='password123', email='jgirliewy@gmail.com', image_url='', )
    seed_user3 = User( username='David Bonkano', password='password123', email='DavidBonk@gmail.com', image_url='', )
    seed_user4 = User( username='Michelle Rose', password='password123', email='Michelleerosey@gmail.com', image_url='', )
    seed_user5 = User( username='Brittany Bleminger', password='password123', email='thebigbrit@gmail.com', image_url='', )
    seed_user6 = User( username='George Plosem', password='password123', email='plosemGeorge10@gmail.com', image_url='', )
    seed_user7 = User( username='Meredith Jordyn', password='password123', email='meredithJordyn@gmail.com', image_url='', )
    
    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()