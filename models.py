from app import db

from sqlalchemy import (
create_engine,
Column,
Integer,
String,
DateTime,
ForeignKey,
Float,
)

from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import settings

engine = create_engine("sqlite:///FAK.db", echo=True)

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Drugs(Base):
    __tablename__ = "Drugs"
    id = Column(Integer, primary_key=True)
    drug_name = Column(String(120))

    def __init__(self, drug_name=None):
        self.drug_name = drug_name

    def __repr__(self):
        return "<Drug {}>".format(self.drug_name)


class Stores(Base):
    __tablename__ = "Stores"
    id = Column(Integer, primary_key=True)
    store_name = Column(String(50))

    def __init__(self, store_name=None):
        self.store_name = store_name

    def __repr__(self):
        return "<Store {}>".format(self.store_name)


class Prices(Base):
    __tablename__ = "Prices"
    id = Column(Integer, primary_key=True)
    date = Column(String(15))
    drug_id = Column(Integer, ForeignKey("Drugs.id"))
    drug = relationship("Drugs")
    store_id = Column(Integer, ForeignKey("Stores.id"))
    store = relationship("Stores")
    price = Column(Float)

    def __init__(self, date=None, drug=None, store=None, price=None):
        self.date = date
        self.drug = drug
        self.store = store
        self.price = price

    def __repr__(self):
        return "<Price {}>".format(self.price)


class URLs(Base):
    __tablename__ = "URLs"
    id = Column(Integer, primary_key=True)
    drug_id = Column(Integer, ForeignKey("Drugs.id"))
    drug = relationship("Drugs")
    store_id = Column(Integer, ForeignKey("Stores.id"))
    store = relationship("Stores")
    drug_url = Column(String(200))

    def __init__(self, drug=None, store=None, drug_url=None):
        self.drug = drug
        self.store = store
        self.drug_url = drug_url

    def __repr__(self):
        return "<URL {}>".format(self.drug_url)

drugs_list = settings.drugs_list


def add_drugs_to_db():
    for i in drugs_list:
        to_db = Drugs(i)
        db_session.add(to_db)

    db_session.commit()

stores_list = settings.stores_list

def add_stores_to_db():
    for i in stores_list:
        to_db = Stores(i)
        db_session.add(to_db)

    db_session.commit()

urls = settings.urls_json

from_json = urls["URLs"]

def add_urls_to_db(from_json):

    for i in from_json:
        drug = Drugs.query.filter(Drugs.drug_name == i['drug_name']).first()
        store = Stores.query.filter(Stores.store_name == i['store_name']).first()
        url = URLs(drug, store, i['drug_url'])

        db_session.add(url)

    db_session.commit()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    add_drugs_to_db()
    add_stores_to_db()
    add_urls_to_db(from_json)
    print("Database created")
    print("Drugs & Stores & URLs filled")