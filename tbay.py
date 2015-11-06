# Author Ryan Kelley

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

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
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bids = relationship('Bid', backref='Item')


class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    auction_item = relationship('Item', backref='user')
    bid = relationship('Bid', backref='bidder')


class Bid(base):
    __tablename__ = "Bids"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)


base.metadata.drop_all(engine)
base.metadata.create_all(engine)

bidder1 = User(username="ryan", password="this is the password")
session.add(bidder1)
session.commit()

bidder2 = User(username="jeff", password="correct battery horse staple")
session.add(bidder2)
session.commit()

bidder3 = User(username="joe", password="correct battery horse cows")
session.add(bidder3)
session.commit()

baseball = Item(name="Baseball for sale", user=bidder1)
session.add(baseball)
session.commit()

bat = Item(name="you need a bat", user=bidder1)
session.add(bat)
session.commit()

bid01 = Bid(price="5.00", bidder=bidder1, Item=baseball)
bid02 = Bid(price="7.00", bidder=bidder2, Item=baseball)
bid03 = Bid(price="6.00", bidder=bidder3, Item=baseball)
session.add_all([bid01, bid02, bid03])
session.commit()

print(session.query(User).all())

print([user.username for user in session.query(User)])
print([item.name for item in session.query(Item)])










