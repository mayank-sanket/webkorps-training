from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Path
from database import engine, SessionLocal
import models
from models import Todos
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field

app = FastAPI()
models.Base.metadata.create_all(bind=engine)   # this happens only if the todos.db file does not exist. If it already exists, then delete it when running the server| better handling is done with migration libraries (not meant for now) | Migration in Alembic Section of the Course



# db dependency:


# could have used async function also
def get_db():
    db = SessionLocal()

    try: 
        yield db 
# only the code prior to and including the yield statement is executed before sending a response
# code following the yield statement is executed after the response is delivered


    # after response
    finally:
        db.close()


# --------------------------------------------------------------------------------------------------------------------

db_dependency = Annotated[Session, Depends(get_db)] # declared it here to use again and again



class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field (gt=0, lt=6)
    completed: bool

# creating async api endpoints

@app.get("/",  status_code=status.HTTP_200_OK )    

# dependency injection 
async def read_all(db: db_dependency):    # Depends(get_db)
    return db.query(Todos).all()
    

@app.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def show_todos_by_id(db: db_dependency, todo_id:int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()  # .first() is used to save costly performance time
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code = 404, detail = "TODO not found")



@app.post("/todos/", status_code=status.HTTP_201_CREATED)
async def add_todo(db:db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**TodoRequest.model_dump())
    db.add(todo_model)
    db.commit()


@app.put("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db:db_dependency, 
                      todo_request: TodoRequest,
                      todo_id: int = Path(gt=0)
                      ):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail= "TODO not found")
    
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.completed = todo_request.completed
    todo_model.priority = todo_request.priority


#     db.add(todo_model)
#     db.commit()


@app.delete("/todos/{todo_id}", status_code= status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency,
                todo_request: TodoRequest,
                todo_id: int = Path(gt=0)):
    todo_model =db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail= "TODO not found")
    
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
    

    # bug to fix 