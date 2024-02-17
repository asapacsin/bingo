from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from pydantic import BaseModel
from typing import Union

class bingo_arr():
    def __init__(self):
        self.len = 99
        self.arr = [i for i in range(1,100)]
        self.record=[]
    def pop(self):
        random_index = random.randint(0,self.len-1)
        get_number = self.arr.pop(random_index)
        self.len -=1
        self.record.append(get_number)
        return get_number
    def reflesh(self):
        self.arr = [i for i in range(1,100)]
        self.record = []
        self.len = 99
    def get_record(self):
        return self.record
    def get_length(self):
        return self.len

class Item(BaseModel):
    name:str
    age:float
    is_TrueMan: Union[bool, None] = None

#initialize an array
arr = bingo_arr()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = "http://localhost:5173/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    if arr.get_length() <= 0:
        return -1
    return arr.pop(), arr

#reflesh request
@app.get("/reflesh/")
def reflesh():
    arr.reflesh()
    return arr

@app.get("/getAll/")
def getAll():
    len = arr.get_length()
    for i in range(len-1):
        arr.pop()
    return arr.pop(), arr

    



##press a button would pop a value from an array


    


