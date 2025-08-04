from pydantic import BaseModel, Field ,field_validator ,EmailStr
from typing import List, Optional ,Dict, Annotated

class patient(BaseModel):
    name: str
    age: int
    email:EmailStr
    # Using Annotated to add metadata to the field
    weight: float
    height: float
    married: bool
    allergies: Optional[list[str]]= None # optional field for allergies
    # Using Dict to represent phone numbers with string keys and values
    phone_numebers:Dict[str,str]

    @field_validator('email') # define the filed_validator decorator for which field
    @classmethod

    def validate_email(cls,value):
        valid_email_domains = ["gmail.com", "yahoo.com", "outlook.com"]
        domain_part=value.split('@')[-1]
        if domain_part not in valid_email_domains:
            raise ValueError(f"Invalid email domain: {domain_part}. Allowed domains are: {', '.join(valid_email_domains)}")
        return value
    @field_validator('name')
    @classmethod
    def validate_age(cls, value):
        
        return value.upper()
    @field_validator('age',mode='before') # mode='before' ensures validation happens before any other processing
    @classmethod
    def validate_age(cls, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        return value
    


def insert_data(patient: patient):
    print(patient.name)
    print(patient.age)
def update_data(patient: patient):
    print(patient.name)
    print(patient.age)  
    print(patient.allergies) 
    print(patient.email) 

patient_data ={"name": "John Doe", "age": 30, "email":"lovelessbhartal12@gmail.com" , "weight": 70.5, "height": 175.0, "married": True, "phone_numebers": {"home": "123-456-7890", "work": "098-765-4321"}}

patient_instance = patient(**patient_data)

insert_data(patient_instance)
update_data(patient_instance)
# This code defines a Pydantic model for a patient and demonstrates how to use it for data validation and manipulation.
# The `insert_data` and `update_data` functions take an instance of the `patient