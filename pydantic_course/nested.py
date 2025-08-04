from fastapi import FastAPI
from pydantic import BaseModel, Field, model_validator, computed_field
class address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class patient(BaseModel):
    name:str
    age:int 
    id:int
    addr:address

adress_dict={"street": "123 Main St", "city": "Springfield", "state": "IL", "zip_code": "62701"}
adress_instance = address(**adress_dict)

patient_data={"name": "John Doe", "age": 30, "id": 1, "addr": adress_instance}
patient_instance = patient(**patient_data)

print(patient_instance.name)
print(patient_instance.age)
print(patient_instance.id)
print(patient_instance.addr.street)
print(patient_instance.addr.city)

temp=patient_instance.model_dump()
print(temp)
print(type(temp))

temp1=patient_instance.model_dump_json()
print(temp1)