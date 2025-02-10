# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import Dict

# app = FastAPI()

# # In-memory storage 
# books: Dict[int, dict] = {}

# # Pydantic model for book validation
# class Book(BaseModel):
#     title: str
#     author: str
#     price: float


# @app.put("/update-book/{book_id}")  # Changed POST to PUT (better for updates)
# def update_book(book_id: int, book: Book):
#     # Check if the book exists
#     if book_id not in books:
#         raise HTTPException(status_code=404, detail="Book not found")  # Correct 404 usage
    
#     # Update the book details
#     books[book_id] = book.model_dump()  # Correct update logic

#     return {"message": "Book updated successfully", "book": books[book_id]}


from fastapi import FastAPI
from fastapi.params import Body




posts = []

app = FastAPI()

@app.get("/")
def root():
    return {f"{posts}"}


@app.post("/createpost")
def create_post(mayank: dict = Body(...)):
    posts.append(mayank)
    print(posts)
    return {f'Post created, {mayank["title"]}, {mayank["content"]}'}


@app.get('/{id}')
def display_posts(id:int):
    return {
        "message": {f"{posts[id]}"}
    }


# restarting the server deletes all the previous things
# therefore, use a database
