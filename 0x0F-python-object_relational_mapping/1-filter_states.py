#!/usr/bin/python3
""" This script lists all states with a name starting with N (upper N)
from the database "hbtn_0e_0_usa"
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MYSQL server
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to list states with name starting with N (upper N)
    qry = "SELECT * FROM `states` WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(qry)

    # Fetch all rows
    states = cursor.fetchall()

    # Print results
    for state in states:
        print(state)

    # Close cursor and database
    cursor.close()
    db.close()
