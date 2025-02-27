from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from models import Users
from typing import Annotated
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from database import SessionLocal
from starlette import status

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta, datetime, timezone

from jose import jwt, JWTError

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated = "auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token') # this parameter contains the url that the client will send to our fastapi application

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

SECRET_KEY='eaa3708340b845171d34c8b43ac2cf81a1ca12d00a218b5c28e575effcf88454'
ALGORITHM='HS256'

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

class Token(BaseModel):
    access_token: str
    token_type: str


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
    return user


def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
        return {'username': username, 'id': user_id, 'user_role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "could not validate user")

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                       create_user_request: CreateUserRequest):
    # create_user_model = Users(**create_user_request.model_dump()) # this will generate error because Users model has a field named hashed_password and we are trying to give it a field called password (createUserRequest)
    
    create_user_model = Users(
        email = create_user_request.email,
        username = create_user_request.username,
        first_name = create_user_request.first_name,
        last_name = create_user_request.last_name,
        role = create_user_request.role,
        hashed_password = bcrypt_context.hash(create_user_request.password),
        is_active = True
    )
    db.add(create_user_model)
    db.commit()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                                      db: db_dependency):
    # return 'token' # dummy
    # return [form_data.username, form_data.password]
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
    # return token
    return {'access_token': token, 'token_type': 'bearer'}










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

# more: 

"""
1. pip install "python-jose[cryptography]"
2. from jose import jwt 
3. create a SECRET_KEY   
        in terminal: openssl rand -hex 32
4. ALGORITHM='HS256'
=> the secret key and algorithm work together to add a signature to the JWT to make sure the JWT is secure and and 
authorized


5. below the authenticate_user function, define a new function create_access_token

"""


# more: 

"""
1. from fastapi.security import OAuth2PasswordBearer
2. oauth2_bearer = OAuth2PasswordBearer(tokenUrl = 'auth/token')
"""