from fastapi import FastAPI, Body
from routers import items
from Config.database import db

app = FastAPI()
app.include_router(items.router)

@app.get("/")
def root():
    return {"msg": "welcome to root page"}

@app.get("/{stdID}")
def get_subject(stdID: int):
    collection = db['enrollment_system']
    data = collection.find_one({'stdID': stdID})
    if data is None:
        return {"msg": "Not found"}
    return data['Course_name']