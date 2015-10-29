__author__ = 'Ryan'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime ,Float

engine = create_engine('postgresql://root:Password!@104.131.148.235:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
base = declarative_base()


class Item(base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    time = Column(DateTime, default=datetime.utcnow)


class User(base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Bid(base):
    __tablename__ = "Bids"

    bid_id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

base.metadata.drop_all(engine)
base.metadata.create_all(engine)

bidder1 = User(username="ryan", password="this is the password")
session.add(bidder1)
session.commit()

bidder2 = User(username="jeff", password="correct battery horse staple")
session.add(bidder2)
session.commit()

baseball = Item(name="Baseball for sale")
session.add(baseball)
session.commit()

bat = Item(name="you need a bat")
session.add(bat)
session.commit()

print(session.query(User).all())

print([user.username for user in session.query(User)])









