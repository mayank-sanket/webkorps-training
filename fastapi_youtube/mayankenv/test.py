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
