from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models import Users
from typing import Annotated
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from database import SessionLocal
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated = "auto")
router = APIRouter(
    tags=["auth"]
)


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str


def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    
    return True



@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                       create_user_request: CreateUserRequest):
    # create_user_model = Users(**create_user_request.model_dump()) # this will generate error because Users model has a field named hashed_password and we are trying to give it a field called password (createUserRequest)
    
    create_user_model = Users(
        email = create_user_request.email,
        username = create_user_request.username,
        first_name = create_user_request.first_name,
        last_name = create_user_request.last_name,
        role = create_user_request.role,
        # hashed_password = create_user_request.password,           # right now not hashing the password
        hashed_password = bcrypt_context.hash(create_user_request.password),
        is_active = True

    )

    # return create_user_model
    db.add(create_user_model)
    db.commit()

@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                                      db: db_dependency):
    # return 'token' # dummy
    # return [form_data.username, form_data.password]
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return "Failed Authentication"
    return "Successful Authentication"











# hashing the password: 
"""
1. pip install passlib
2. install a specific version of bcrypt : pip install bcrypt==4.0.1

3. in the auth.py file: from passlib.context import CryptContext

# bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated = "auto")
"""





# gettting the username and password for login 

"""
1. install python-multipart (pip install python-multipart)
2. we will use OAuth2   : from fastapi.security import OAuth2PasswordRequestForm
3. now we need to use OAuth2PasswordRequestForm as a dependency injection in our api endpoint

"""