#!/usr/bin/python3
"""
 adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def addObj(uname, pword, db):
    """a class that adds the State object
    “Louisiana” to the database hbtn_0e_6_usa"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(uname, pword, db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    obj = State(name="Louisiana")
    session.add(obj)
    session.commit()
    session.close()
    print(obj.id)


if __name__ == "__main__":
    uname = argv[1]
    pword = argv[2]
    db = argv[3]
    addObj(uname, pword, db)
