__author__ = 'Ryan'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine('postgresql://root:Password!@104.131.148.235:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
base = declarative_base()


class Item(base):
    __tablename__ = "items"

    id = Column(id, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    time = Column(datetime, default=datetime.utcnow)

    Base.metadata.create_all(engine)







