from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import AbstractConcreteBase

# cria uma classe Base para o instanciamento de novos objetos/tabelas

class Base(DeclarativeBase):
    pass