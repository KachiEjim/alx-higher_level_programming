#!/usr/bin/python3

"""A script to list all states from the hbtn_0e_0_usa database.
Usage:
    python list_states.py <username> <password> <database>
"""

import MySQLdb
from sys import argv



def listStates(username, password, database, state_name):
    """List all states from the hbtn_0e_0_usa database.
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

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(argv == 5):
        username = argv[1]
        password = argv[2]
        database = argv[3]
        state_name = argv[4]
        listStates(username, password, database, state_name)
