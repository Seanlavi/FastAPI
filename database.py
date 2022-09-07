from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db" # incase ill prefer using a smaller data base (sqlite3)
'''

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:S1s2s3s4s5!@localhost/TodoAppDataBase"  # (postgres)

'''
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:S1s2s3s4s5!@127.0.0.1:3306/todoapp"  # mySql
'''
engine = create_engine(
    SQLALCHEMY_DATABASE_URL  # ,connect_args={"check_same_thread": False} - "a specific line for Sqlite3"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
