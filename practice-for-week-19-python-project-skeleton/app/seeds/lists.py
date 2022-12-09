from app.models import db, List, environment, SCHEMA


def seed_lists():
    list1 = List(name='Groceries', user_id=1, due='2023-06-01')
    list2 = List(name='Household Chores', user_id=1, due='2023-06-01')
    list3 = List(name='Yardwork', user_id=1, due='2023-06-01')
    list4 = List(name='Group Project', user_id=1, due='2023-05-03')

    db.session.add(list1)
    db.session.add(list2)
    db.session.add(list3)
    db.session.add(list4)




    db.session.commit()

def undo_lists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.lists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM lists")

    db.session.commit()