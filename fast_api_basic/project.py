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
@app.get('/view/{patient_id}')
def view_patient(patient_id: int):
    data = load_data()
    patient = next((p for p in data if p['id'] == patient_id), None)
    if patient:
        return {"patient": patient}
    else:
        return {"error": "Patient not found"}