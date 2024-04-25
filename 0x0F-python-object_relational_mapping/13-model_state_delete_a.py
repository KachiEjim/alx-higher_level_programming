#!/usr/bin/python3
"""
deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def deleteAll(uname, pword, db):
    """a function that deletes all State objects with a name containing the
    letter a from the database hbtn_0e_6_usa
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        uname, pword, db), pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()


if __name__ == "__main__":
    u = argv[1]
    p = argv[2]
    d = argv[3]
    deleteAll(u, p, d)
