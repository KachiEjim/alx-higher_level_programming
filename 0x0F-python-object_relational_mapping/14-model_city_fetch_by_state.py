#!/usr/bin/python3
"""prints all City objects from
the database hbtn_0e_14_usa:"""

from sys import argv
from model_city import Base, City
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



def fetchCity(uname, pword, db):
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        uname, pword, db), pool_pre_ping=True)
    
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    cities = session.query(City, State).filter(City.state_id == State.id).order_by(City.id)
    print(cities)
    for city, state in cities:
        print(f"{state.name}: {(city.id)} {city.name}")


if __name__ == "__main__":
    u = argv[1]
    p = argv[2]
    d = argv[3]
    fetchCity(u, p, d)

