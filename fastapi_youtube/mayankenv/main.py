from fastapi import FastAPI, Path, HTTPException
app = FastAPI()
from typing import Optional, Dict
from pydantic import BaseModel
from employees import employees
from students import students

from players import players




@app.get('/')
def get_index():
    return {"message": "Welcome to the website!"}


@app.get('/employees/{emp_id}')
def get_employee_by_id(emp_id:int):
    return employees[emp_id]

# Path parameters
@app.get('/students/{s_id}')
def get_student_by_id(s_id: int = Path(..., description="ID of the student you want to view", gt=0, lt=13)):
    return students[s_id]

# Query Parameters
# eg: google.com/results?search=Python

@app.get("/get-by-name")
def get_student(name: str):
    for student in students:
        if(students[student]["name"].lower() == name): 
            return students[student]
    return {'Data': 'No student with the name you entered'}






# making query parameters optional
# 1st way: name: str = None
# 2nd way (recommended): name Optional[str] = None  | but do this first => from typing import Optional


# note: in case of multiple queries
# this will throw an error: def fxn_name (name: Optional[str] = None, test: int)     because required parameters should be before the optional ones    | how to avoid this?
# do this: 1st way:  def fnx_name(test: int, name: Optional[str] = None)
# do this: 2nd way (better) : (*, name: Optional[str] = None, test: int)


@app.get('/testurl/')
def get_test_student(test:int, name: Optional[str] = None):
    if not name:
        return f"test query {test}"
    
    else:
        for st in students:
            if(students[st]['name'].lower() == name):
                ax = students[st]
      
    return {
        'stdnt': ax,
        'testquery': test
    }


# combining query and path parameters together

@app.get('/get-by-name-combined/{student_id}')
def get_std_comb(*, student_id: int, test: int, name: Optional[str] = None):
         if student_id:
             a = students[student_id]
             return {
                 "student_object": a,
                 "test": test*10,
                 "name": students[student_id]["name"]
             }
         else:
             return {'data': "invalid request"}





# Rquest Body and Post Method

# for this, you need to import BaseModel from pydantic

    # do later ()