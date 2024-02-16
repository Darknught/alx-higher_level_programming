#!/usr/bin/python3
""" This script list all states from the database "hbtn_0e_0_usa."""


import MySQLdb
import sys


def list_states(username, password, database):
    # Connect to MYSQL server
    db = MYSQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select all states and sort them by id
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all rows
    states = cursor.fetchall()

    # Print results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
