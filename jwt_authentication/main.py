from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import UserModel  # Renamed to avoid conflict
from schemas import UserCreate, UserResponse, Token, UserUpdate
from auth import get_password_hash, verify_password, create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta


UserModel.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = UserModel(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    

    user = db.query(UserModel).filter(UserModel.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=UserResponse)
def read_users_me(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == current_user["email"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/me", response_model=UserResponse)
def update_user(
    user_update: UserUpdate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_user = db.query(UserModel).filter(UserModel.email == current_user["email"]).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    
    if user_update.email and user_update.email != db_user.email:
        
        existing_user = db.query(UserModel).filter(UserModel.email == user_update.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        db_user.email = user_update.email
    
    
    if user_update.password:
        db_user.hashed_password = get_password_hash(user_update.password)
    
    
    if user_update.is_active is not None:
        db_user.is_active = user_update.is_active
    
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/me", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    import pdb;pdb.set_trace()
    db_user = db.query(UserModel).filter(UserModel.email == current_user["email"]).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted"}