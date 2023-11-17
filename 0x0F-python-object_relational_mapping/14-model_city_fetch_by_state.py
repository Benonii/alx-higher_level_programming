#!/usr/bin/python3

'''  lists all State objects from the database hbtn_0e_6_usa '''
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).join(City).filter(
                     State.id == City.state_id).order_by(City.id).all()

    for row in result:
        print(f"{row.State.name}: ({row.City.id}) {row.City.name}")
