from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, field_computed
from typing import Annotated
import os
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID of the patient", example="p001")]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="Where the patient lives")]
    age: Annotated[int, Field(..., gt=0, lt=100, description="Age of the patient")]
    gender: Annotated[str, Field(..., description="Gender of the patient")]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient")]
    weight: float

    @field_computed()
    @property
    def bmi(self) -> float:
      return round(self.weight / (self.height / 100) ** 2, 2)

    @field_computed()
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "underweight"
        elif self.bmi < 25:
            return "normal"
        elif self.bmi < 30:
            return "overweight"
        else:
            return "obese"

def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(file_path, "r") as f:
        return json.load(f)

@app.get('/')
def hello():
    return {"message": "This is the patient management system"}

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

@app.get('/patient/{patient_id}')
def view_patient(
    patient_id: str = Path(..., title="Patient ID", description="The ID of the patient to view")
):
    data = load_data()
    if patient_id in data:
        return {"patient": data[patient_id]}
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., title="Sort By", description="Sort patients by name or age"),
    order: str = Query("asc", title="Order", description="Sort order, either 'asc' or 'desc'")
):
    data = load_data()
    if sort_by not in ["name", "age"]:
        raise HTTPException(status_code=400, detail="Invalid sort parameter")
    
    sorted_patients = sorted(data.items(), key=lambda x: x[1][sort_by])
    if order == "desc":
        sorted_patients.reverse()

    return {"sorted_patients": dict(sorted_patients)}
