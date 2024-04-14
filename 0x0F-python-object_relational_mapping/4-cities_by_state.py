#!/usr/bin/python3

"""A script to list all cities from the hbtn_0e_4_usa database.
Usage:
    python list_cities.py <username> <password> <database>
"""

import MySQLdb
from sys import argv


def listCities(username, password, database):
    """List all cities from the hbtn_0e_4_usa database.
    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the MySQL database.

    Returns: None
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cursor = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        database = argv[3]
        listCities(username, password, database)
