from fastapi import FastAPI, Body
app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/")
async def index():    # async is optional for fastapi

    return {
        "message": "Hello, Mayank"
    }

# api-endpoints
# order matters with path parameters

# path parameters

@app.get("/books")
async def read_all_books():
    return BOOKS



@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

# request url: 127.0.0.1:8000/books/title%20four     #    %20 means space





# @app.get("/books/mybook")
# async def read_all_books():
#     return {"book title": "my favourite book"}

# @app.get("/books/{dynamic_param}")  # dynamic parameter
# async def read_all_books(dynamic_param: str):
#     return {"dynamic param": dynamic_param}


# @app.get("/books/mybook") # static parameter
# async def read_all_books():
#     return {"book title": "My favourite book"}   # note : it still returns {"dynamic param": dynamic param}  because it behves like dynamic param due to placement of code block

# therefore, place this above the dynamic path parameter 




@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:  
        if book.get('title').casefold() == book_title.casefold():
            return book
        





#query parameters:


@app.get("/books/")    # /book is a path param
async def read_category_by_query(category: str):   # category is a query
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    
    return books_to_return


@app.get("/books/byauthor/")  
async def read_books_by_author(author:str): # author is passed via query
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
        book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    
    return books_to_return



# get request do not  have a body

# a post request has a body

# to send request body, you need to import Body from fastapi

@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)    



@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book



@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if book_title.casefold() == BOOKS[i].get('title').casefold():
            BOOKS.pop(i)
            break





# assignment: create a new API endpoint that can fetch all books from a specific author using either path parameter or query parameter










# path parameter

@app.get("/books/byauthor/{author}")
async def read_books_by_author_path (author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


# query parameter

# @app.get("/books/byauthor/")  # placing it here will cause error, therefore take it above path parameter (which has similar path and expects one more query) -- now placed at line 85

# async def read_books_by_author(author:str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('author').casefold() == author.casefold():
#             books_to_return.append(book)
#     return books_to_return



# note: good practice: keep smaller api endpoints at the front of the code