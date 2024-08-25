from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import URL
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.album import Album

db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
   # então cria o diretorio
   os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
url_object = URL.create(
    "postgresql+pg8000",
    username="postgres",
    password="postgres",
    host="localhost",
    database="dbteste",
)
url = 'postgresql+psycopg2://postgres:postgres@192.168.15.138/dbteste?port=5432'
# cria a engine de conexão com o banco
engine = create_engine(url)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)
