#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
Usage: ./9-model_state_filter_a.py <mysql username> /
                                   <mysql password> /
                                   <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


def fetchAll(username, password, dbname):
    """a class that lists all State objects from the
    database hbtn_0e_6_usa

    Attributes:
    username (str): Username of the user
    password (str): user password
    dbname (str): Database to be assessed
    """

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    fetchAll(username, password, dbname)
