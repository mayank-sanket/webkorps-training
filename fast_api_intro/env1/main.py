from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello, Mayank!'}


# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = None


# @app.post('/items/')
# def create_item(item:Item):
#     return item

@app.get('/contact-us')
def display_contact():
    return {'message': '+91 9267983805'}



@app.get('/testpage')
def display_homepage():
    return {'msg': 'hi there'}