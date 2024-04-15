#!/usr/bin/python3
"""
Prints the State object with the name passed
as argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def fetchStateByName(username, password, dbname, state_name):
    """Fetches the State object by name from the database.
    Attributes:
        username (str): Username of the user
        password (str): user password
        dbname (str): Database to be assessed
        state_name (str): name of the state
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, dbname),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    for state in states:
        if state_name == state.name:
            print("{}".format(state.id))
            break
    else:
        print("Not found")


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    fetchStateByName(username, password, dbname, state_name)
