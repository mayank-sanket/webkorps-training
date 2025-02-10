from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello, Mayank!'}




@app.get('/contact-us')
def display_contact():
    return {'message': '+91 9267983805'}



@app.get('/testpage')
def display_homepage():
    return {'msg': 'hi there'}




# note: always place this type of endpoint above the "/blogs/{id}" or "/blogs/{id}/comments" endpoints because 
# if not done like this, then the int-string confusion will lead to errors/unexpected behaviours
@app.get("/blogs/unpub")
def show_unpublished():
    return {"data": "All unpublished blogs here"}




@app.get('/blogs/{id}')
def show_blogs(id:int):
    return {
        "content": f"Blog with the id {id} is here"
    }


@app.get("/blogs/{id}/comments")
def show_comments(id:int):
    return [
        "comment 1",
        "comment 2",
        "comment 3"
    ]



#query parameters (hard coded example)

@app.get("/blogs?limit=10&published=true")   # 
def show_blogs():
    # only get 10 published blogs
    return {"data": "10 published blogs"}


@app.get("/blogs/")
def show_limited_blogs(limit:int, published: bool):     # can go without type validation but sometimes the output is not what we want like, therefore always recommended to use types

    # by default the parameters are required and if you don't enter the parameter, you get an error
    # to prevent the error, you can make the paramters optional also
     
    # also you can use default values: like limit=10 (while defining the show_limited_blogs function)

    if published:
        return {"data": f"Blog List of {limit} PUBLISHED blogs"}
    else: 
        return {"data": f"Blog list of {limit} blogs which are not published"}

    

# now if you enter url like: /blogs?limit=14, then you get corresponding data


@app.get("/posts/")
def show_posts(limit:int = 10, published:bool = True):   # note, if the leftmost query has a default value, the other ones (if they are required) must also have some  default values
# def show_posts(published:bool, limit:int=10) 
    if published:
        return {"data": f"Here are the {limit} published posts"}
    else:
        return {"data": f"Here are the {limit} posts which may or may not be published"}
    

#optional parameters
@app.get("/works")
def show_works(published:bool, limit:int =  10, sort:Optional[str] = None): # from typing import Optional
    if sort:
        return f"hello there, the data is sorted"
    



# POST METHOD

# sample 
@app.post("/blogposttest")
def create_blog():
    return {"data": "Blog is created"}



# actual
class Blog(BaseModel):   # from pydantic import BaseModel
    title: str
    body: str
    published: Optional[bool] = None

@app.post("/blogs")
def create_blog(blog: Blog):
    return {"data": f"Blog created with title as {blog.title}"}






























# what if you want to run the server on some other port?
import uvicorn # at the top
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="7500")

# now you can run simply by : python3 main.py