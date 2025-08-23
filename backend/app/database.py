import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine(os.environ.get("DATABASE_URL"))
Session = scoped_session(sessionmaker(bind=engine))

def init_db(app):
    with app.app_context():
        Base.metadata.create_all(bind=engine)