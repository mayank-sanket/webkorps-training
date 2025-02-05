from fastapi import FastAPI
app = FastAPI()


# @app.get('/')
# def index():
#     return 'hey'  # "hey"


# @app.get('/')
# def index():
#     return {'message': 'Hey there!'}

@app.get('/')
def index():
    return {'data': {'name': 'Mayank Sanket', 'age': 23, 'department': 'Tech'}}

@app.get('/about')
def about():
    # return {'data': {'about page'}} # data ['about page']
    return {'data': 'about page'}

@app.get('/blogs/{id}')
def blogs(id:int):
    return {'data': id} # retuns like {'data': '4}



@app.get('/numblogs/{id}')
def numblogs(id:int):
    return {'data': id} # returns  like {'data': 4}


@app.get('/blogs/{id}/comments')
def comments(id):
    
    # fetch comments of blog with id = id

    return {
        'data': {
            'comments': ['comment 1', 'comment 2']
        }
    }

