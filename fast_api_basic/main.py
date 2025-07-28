from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
@app.get("/")
def hello():
    return {"message": "Hello, World!"}
@app.get("/about_code")
def about_code():
    return {
        "name": "FastAPI Example"}
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Item ID must be a positive integer")
    return {"item_id": item_id, "q": q}
