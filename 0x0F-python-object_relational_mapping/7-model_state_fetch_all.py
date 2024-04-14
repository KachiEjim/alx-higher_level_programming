#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
Usage: ./7-model_state_fetch_all.py <mysql username> /
                                    <mysql password> /
                                    <database name>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetchAll(username, password, dbname):
    """a class that lists all State objects from the
    database hbtn_0e_6_usa

    Attributes:
    username (str): Username of the user
    password (str): user password
    dbname (str): Database to be assessed
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(username, password, dbname),
        pool_pre_ping=True
    )
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    states = session.query(State).order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    fetchAll(username, password, dbname)
