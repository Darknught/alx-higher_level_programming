#!/usr/bin/python3
""" A script that takes in an argument and displays all values in the `states`
table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys


if __name__ == "__main__":
    state_name = sys.argv[4]
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select states with matching name
    q = "SELECT cities.id, cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(q, (state_name,))

    # Fetch all rows
    cities = cursor.fetchall()

    # Print results
    for city in cities:
        print(city)

    # Close cursor and database
    cursor.close()
    db.close()
