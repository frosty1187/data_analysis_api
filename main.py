from typing import Optional

from fastapi import FastAPI
import pandas as pd
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:*",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




class test:
    df = []
    def __init__(self, location):
        self.df = pd.read_csv(location).replace('"','', regex=True)
        self.df.columns = [f.replace('"','') for f in self.df.columns]
        self.df = self.df.fillna('NaN')
        print(self.df)

    

tst = test("./data/nile.csv")

@app.get("/test/repeat/{orientation}")
def return_df(orientation:str):
    print(tst.df.to_json(orient=orientation))
    return {'data':tst.df.to_dict(orient=orientation)}

@app.get("/test/columns")
def return_df():
    print(tst.df.columns)
    return {"columns": list(tst.df.columns)}

@app.get("/test/describe/{orientation}")
def return_df(orientation:str):
    print(tst.df.columns)
    return {"columns": tst.df.describe().to_dict(orient=orientation)}


@app.get("/test/save")
def return_df():
    print(tst.df.columns)
    return {"columns": list(tst.df.columns)}

@app.get("/test/load/{file}/{orientation}")
def return_df(file:str,orientation:str):
    tst = test(f"./data/{file}.csv")
    return {'data':tst.df.to_dict(orient=orientation)}
