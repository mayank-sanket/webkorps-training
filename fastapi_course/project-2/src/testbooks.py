from fastapi import FastAPI, Body
app = FastAPI()
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self. author = author
        self.description = description
        self.rating = rating

# books is a list of objects created from the Book class
books = [
Book(1, 'Computer Science Pro', 'Mayank Sanket', 'A book which teaches you Computer Science from beginner level to advanced level', 5),
Book(2, 'Our World Then and Now', 'Samir Sharma', 'History book ', 4), 
Book(3, 'Problems in General Physics', 'IE Irodov', 'A book for problems in general physics written by IE Irodov', 5),
Book(4, 'Physics Volume 1', 'HC Verma', 'Used by millions of students preparing for JEE Main and Advanced', 5),
Book(5, 'Algebra', 'G Tewani', 'A mathematics book of the famous series by G Tewani', 4),
Book(6, 'Do Epic Shit', 'Ankur Warikoo', 'A great book by Ankur Warikoo', 4),
Book(7, 'Get Epic Shit Done', 'Ankur Warikoo', 'Another great book by Ankur Warikoo', 4)
]

@app.get("/")
async def index():
    return {"message": "Welcome to the page!"}

@app.get("/books")
async def read_all_books():
    return books

@app.post("/create-book")
async def create_books(book_request = Body()):
    books.append(book_request)

# note:  using Body we could not validate data (eg: rating between 1 and 5; id being serial incremental, etc)
# for that we need to use Pydantic