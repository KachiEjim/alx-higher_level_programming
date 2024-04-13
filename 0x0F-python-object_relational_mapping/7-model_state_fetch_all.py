#!/usr/bin/python3
"""
A script that lists all cities of a given state from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


def filterCities(username, password, database, state_name):
    """
    List all cities of a given state from the hbtn_0e_4_usa database.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the MySQL database.
        state_name (str): The name of the state to filter cities.

    Returns:
        None
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cursor = db.cursor()

    query = """
        SELECT cities.name
        FROM cities states
        ORDER BY cities.id
    """
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    result =", ".join([row[0] for row in rows])

    print(result)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) == 5:
        username = argv[1]
        password = argv[2]
        database = argv[3]
        state_name = argv[4]
        filterCities(username, password, database, state_name)
