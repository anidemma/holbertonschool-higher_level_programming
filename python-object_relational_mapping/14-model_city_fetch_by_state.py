#!/usr/bin/python3
"""Cities in state"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_city import City
from model_state import State

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(City, State).join(State)

    for _c, _s in query.all():
        print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))

    session.commit()
    session.close()
