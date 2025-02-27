from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey



class Users(Base):
    __tablename__ ='users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)






class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    


# install and configure sqlite3
# open todos.db file with sqlite3 : sqlite3 todos.db

# see schema:   .schema
# see mode: .mode
# modes examples: .mode column, .mode list, .mode csv


# note: if the row with id 4 is deleted and then a new row is inserted after it, it gets the id value equal to 4
