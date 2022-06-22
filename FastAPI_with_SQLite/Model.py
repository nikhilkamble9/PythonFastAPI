from sqlalchemy import Column, Float, Integer, String
from db_handler import Base


class Address(Base):

    __tablename__ = "address"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    pincode = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    maplink = Column(String)
