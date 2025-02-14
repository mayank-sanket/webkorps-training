from database import Base
from sqlalchemy import Column, Integer, String, Boolean
class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean, default=False)


# install and configure sqlite3
# open todos.db file with sqlite3 : sqlite3 todos.db

# see schema:   .schema
# see mode: .mode
# modes examples: .mode column, .mode list, .mode csv


# note: if the row with id 4 is deleted and then a new row is inserted after it, it gets the id value equal to 4
