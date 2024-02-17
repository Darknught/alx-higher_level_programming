#!/usr/bin/python3
"""
A script that creates the  State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database}"
            )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State and City
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add the new State and City to the session and commit the transaction
    session.add(new_state)
    session.add(new_city)

    session.commit()

    # Close session
    session.close()
