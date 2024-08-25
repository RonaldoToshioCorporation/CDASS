from model import Base
from sqlalchemy import Column, String, Integer,ForeignKey , Numeric
from sqlalchemy.ext.declarative import AbstractConcreteBase

class Album(Base):
    __tablename__ = 'album'
    id = Column("id", Integer, primary_key=True)
    title = Column("title", String(100))
    artist = Column("artist", String(100))     
    price = Column("price", Numeric(precision=2, asdecimal=True, decimal_return_scale=None))

    #criar Album
    def __init__(self, 
                 id: Integer,
                 title: String,
                 artist: String,
                 price: String):
        self.id = id
        self.title = title
        self.artist = artist
        self.price = price