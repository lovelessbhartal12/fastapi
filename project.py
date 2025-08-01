from fastapi import FastAPI
import json
app = FastAPI()
def load_data():
    with open("patients12.json", "r") as f:
        jasion_data = json.load(f)
    return jasion_data
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
@app.get('/view_patients')
def view_patients():
    data = load_data()
    return {"patients": data}