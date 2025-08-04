from fastapi import FastAPI, Path , HTTPException ,Query
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
#path parameter
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str= Path(..., title="Patient ID", description="The ID of the patient to view")):
    data=load_data()

    if patient_id in data:
        return {"patient": data[patient_id]}
    raise HTTPException(status_code=404, detail="Patient not found")
#query parameter
@app.get('/sort')
def sort_patients(sort_by: str =Query(..., title="Sort By", description="Sort patients by name or age"), order: str = Query("asc", title="Order", description="Sort order, either 'asc' or 'desc'")):
    data = load_data()
    if sort_by not in ["name", "age"]:
        raise HTTPException(status_code=400, detail="Invalid sort parameter")
    
    sorted_patients = sorted(data.items(), key=lambda x: x[1][sort_by])
    return {"sorted_patients": {k: v for k, v in sorted_patients}}
    