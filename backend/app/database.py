import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.base import Connection
from .models import Base

# Database setup
engine = create_engine(os.environ.get("DATABASE_URL"))
Session = sessionmaker(bind=engine)