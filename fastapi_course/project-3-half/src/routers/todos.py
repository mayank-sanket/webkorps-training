from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path
from database import SessionLocal
from models import Todos
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field

from .auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()

    try: 
        yield db 
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)] # declared it here to use again and again
user_dependency = Annotated[dict, Depends(get_current_user)]


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field (gt=0, lt=6)
    completed: bool


@router.get("/",  status_code=status.HTTP_200_OK )    

async def read_all(db: db_dependency):  
    return db.query(Todos).all()
    

@router.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def show_todos_by_id(db: db_dependency, todo_id:int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()  # .first() is used to save costly performance time
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code = 404, detail = "TODO not found")



@router.post("/todo/", status_code=status.HTTP_201_CREATED)
async def add_todo(user: user_dependency, db:db_dependency, todo_request: TodoRequest):
    if user is None: 
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model = Todos(**todo_request.model_dump(), owner_id=user.get('id')) # the part after comma gave error, idk why
    
    
    db.add(todo_model)
    db.commit()
    

@router.put("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
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


    db.add(todo_model)
    db.commit()


@router.delete("/todos/{todo_id}", status_code= status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency,
                
                todo_id: int = Path(gt=0)):
    todo_model =db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail= "TODO not found")
    
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
   


