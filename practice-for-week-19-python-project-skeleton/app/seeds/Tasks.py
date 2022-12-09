from app.models import Tasks, db


def seed_items():
    task1 = Tasks(
        name='Buy my starbies', user_id=1, due='2030-10-92', notes='Grind Coffee', list_id=1 )
    task2 = Tasks(
        name='Buy some cat food', user_id=1, due='2030-10-92', notes='Must be vegan, fair trade, and from Colombia', list_id=1 )
    task3 = Tasks(
        name='Buy some cat food', user_id=1, due='2030-10-92', notes='Must be vegan, fair trade, and from Colombia', list_id=1 )

    db.session.add(task1)
    db.session.add(task2)
    db.session.add()
    db.session.commit()