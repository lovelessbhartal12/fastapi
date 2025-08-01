from fastapi import FastAPI
import json
app = FastAPI()
import os
import json

def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(file_path, "r") as f:
        return json.load(f)

@app.get('/')
def hello():
    return {"message": "This is the patitent management system"}
@app.get('/about')
def about():
    return {
        "name": "Patient Management System",
        "version": "1.0.0",
        "description": "A simple API for managing patient records"
    }
@app.get('/view')
def view():
    data = load_data()
    return {"patients": data}