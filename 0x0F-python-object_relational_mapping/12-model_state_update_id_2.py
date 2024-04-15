#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def changeName(uname, pword, db):
    """A class that changes the name of a
    State object from the database hbtn_0e_6_usa"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(uname, pword, db),
                           pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()


if __name__ == "__main__":
    u = argv[1]
    p = argv[2]
    d = argv[3]
    changeName(u, p, d)
