#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
Usage: ./9-model_state_filter_a.py <mysql username> /
                                   <mysql password> /
                                   <database name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def fetchWithA(username, password, dbname):
    """ that lists all State objects that contain the
    letter a from the database hbtn_0e_6_usa

    Attributes:
        username (str): Username of the user
        password (str): user password
        dbname (str): Database to be assessed
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, dbname),
                           pool_pre_ping=True)
    Session_maker = sessionmaker(bind=engine)
    session = Session_maker()
    states = session.query(State).order_by(State.id)
    for state in states:
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    fetchWithA(username, password, dbname)
