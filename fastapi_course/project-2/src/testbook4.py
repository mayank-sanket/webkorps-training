# motive: implementing HTTPExceptions


from fastapi import FastAPI, Body, Path, Query, HTTPException
# Imported Path to validate Path parameters
# Imported Query to validate Query parameters
# Importted HTTPException for raising HTTPExceptions
from typing import  Optional
from pydantic import BaseModel, Field

app = FastAPI()



class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int


    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self. author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date



class BookRequest(BaseModel):
    # id: Optional[int] = None           # made it optional so that even if it is not passed, it does not create an error
    id: int = Field(description='ID is not needed on create', default=None) # added field validation as well as optional type
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=300)
    rating: int = Field(gt=-1, lt=6)  # 0 to 5
    published_date: int = Field(gt=1990, lt=2400)   




    # model_config  (for swagger docs example section)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Author's name",
                "description": "Book's description",
                "rating": 5,
                "published_date": 2020            }
        }
    }


BOOKS = [
Book(1, 'Computer Science Pro', 'Mayank Sanket', 'A book which teaches you Computer Science from beginner level to advanced level', 5, 2021),
Book(2, 'Our World Then and Now', 'Samir Sharma', 'History book ', 4, 2023), 
Book(3, 'Problems in General Physics', 'IE Irodov', 'A book for problems in general physics written by IE Irodov', 5, 1912),
Book(4, 'Physics Volume 1', 'HC Verma', 'Used by millions of students preparing for JEE Main and Advanced', 5, 2007),
Book(5, 'Algebra', 'G Tewani', 'A mathematics book of the famous series by G Tewani', 4, 2010),
Book(6, 'Do Epic Shit', 'Ankur Warikoo', 'A great book by Ankur Warikoo', 4, 2020),
Book(7, 'Get Epic Shit Done', 'Ankur Warikoo', 'Another great book by Ankur Warikoo', 4, 2019)

]




@app.get("/")
async def index():
    return {"message": "Welcome to the page!"}


@app.get("/books")
async def read_all_books():
    return BOOKS


        

@app.get("/books/publish")   # assignment solution
async def books_by_publish_date(published_date: int = Query(gt=1900, lt=2400)):
    books_to_return = []
    for book in BOOKS:
        if int(book.published_date) == published_date:
            books_to_return.append(book)
    return books_to_return


# validation inside path parameter
@app.get("/books/{book_id}")
async def show_book_by_id(book_id: int = Path(gt=0, lt=100)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail= "Item not found")
    

# fetching book by query parameter id

@app.get("/books/")   # here the order does not cause much harm as this endpoint uses query parameter
async def show_book_by_rating(rating:int = Query(lt=6, gt=-1)):
    books_to_return = []
    for book in BOOKS: 
        if book.rating == rating:
            books_to_return.append(book)
    return books_to_return
        




# @app.post("/create-book")
# async def create_books(book_request: BookRequest):
#     print(type(book_request))              # class <class 'books.BookRequest'>
#     BOOKS.append(book_request)  


# the above part also works, but the below is better:

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump()) # (pydantic version 2)                    # in pydantic version 1, .dict() is used instead of model_dump()
    # print(type(new_book))  # < class 'books.Book'>
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):   # not async     (for auto-increment of IDs)
    # if len(BOOKS) > 0: 
    #     book.id = BOOKS[-1].id + 1
    # else: 
    #     book.id = 1

    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1 
    return book





@app.put("/books/update_book")
async def update_book(book:BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
        

        
        if not book_changed:
            raise HTTPException(status_code=404, detail="No BOOK with the entered ID(item not found)")



# validating path parameter
@app.delete("/books/{book_id}")
async def delete_book_by_id(book_id:int = Path(gt=0, lt=100)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    
    if not book_changed: 
        raise HTTPException(status_code=404, detail="Item not found")



