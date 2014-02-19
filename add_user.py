#!/usr/bin/python
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from chaser.models import User
from settings.settings import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)


def main(argv):
    Session = sessionmaker(bind=engine)
    session = Session()
    session._model_changes = {}
    try:
        session.add(User(user_name=argv.user, password=argv.password))
    finally:
        session.commit()
        session.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    main(args)
