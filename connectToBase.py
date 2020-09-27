from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine.url import URL
import psycopg2
from sqlalchemy.ext.declarative import declarative_base


DeclarativeBase = declarative_base()


class Post(DeclarativeBase):
    __tablename__ = 'filepath'
    id = Column(Integer, primary_key=True)
    clientName = Column('client_name', String)
    filePathToKP = Column('file_path_to_kp', String)
    filePathToContract = Column('file_path_to_contract', String)


DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'VjqGfhjkm',
    'database': 'postgres'
}


def connect():
    engine = create_engine(URL(**DATABASE))
    DeclarativeBase.metadata.create_all(engine)
    con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="VjqGfhjkm",
        host="127.0.0.1",
        port="5432",
    )
    return con
