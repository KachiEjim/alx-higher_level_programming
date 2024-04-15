#!/usr/bin/python3
""" a script that creates the State
“California” with the City “San Francisco” from the database
hbtn_0e_100_usa: (100-relationship_states_cities.py)"""

from sys import argv as a
from sqlalchemy import create_engine
from sqlachemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(a[1], a[2], a[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
