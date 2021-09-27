from .model import *

def insert_data(db):
    try:
        '''
        Ivan = User(username="Ivan Ivanov")
        Piotr = User(username="Piotr Petrovich")
        Sidor = User(username="Sidor Sidorovich")

        db.session.add(Ivan)
        db.session.add(Piotr)
        db.session.add(Sidor)

        lead1 = Leader()
        Ivan.leader = lead1
        db.session.add(lead1)
        lead2 = Leader()
        Piotr.leader = lead2
        db.session.add(lead2)
        lead3 = Leader()
        Sidor.leader = lead3
        db.session.add(lead3)

        Coffee = Task(name="Coffee", text="kupit kofe", deadline="zavtra")
        Tea = Task(name="Tea", text="kupit chai", deadline="zavtra")
        Plants = Task(name="Plants", text="polit cveti", deadline="segodnya")

        db.session.add(Coffee)
        db.session.add(Tea)
        db.session.add(Plants)

        Supplies = Project(name="Supplies")
        Greenery = Project(name="Greenery")
        Work = Project(name="Actual Work")

        db.session.add(Supplies)
        db.session.add(Greenery)
        db.session.add(Work)

        Ivan.tasks = Coffee
        Piotr.tasks = Tea
        Sidor.tasks = Plants

        Ivan.projects = Supplies
        Piotr.projects = Supplies
        Sidor.projects = Greenery

        Coffee.projects = Supplies
        Tea.projects = Supplies
        Plants.projects = Greenery
        '''
        db.session.commit()
    except Exception:
        pass
