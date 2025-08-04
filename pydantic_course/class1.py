from pydantic import BaseModel, Field
from typing import List, Optional ,Dict

class patient(BaseModel):
    name: str = Field(..., title="Patient Name", description="The name of the patient")
    age: int = Field(..., title="Patient Age", description="The age of the patient")
    weight: float
    height: float
    married: bool
    allergies: Optional[list[str]]= None # optional field for allergies
    # Using Dict to represent phone numbers with string keys and values
    phone_numebers:Dict[str,str]



def insert_data(patient: patient):
    print(patient.name)
    print(patient.age)
def update_data(patient: patient):
    print(patient.name)
    print(patient.age)  
    print(patient.allergies)  

patient_data ={"name": "John Doe", "age": 30, "weight": 70.5, "height": 175.0, "married": True, "phone_numebers": {"home": "123-456-7890", "work": "098-765-4321"}}

patient_instance = patient(**patient_data)

insert_data(patient_instance)
update_data(patient_instance)
# This code defines a Pydantic model for a patient and demonstrates how to use it for data validation and manipulation.
# The `insert_data` and `update_data` functions take an instance of the `patient