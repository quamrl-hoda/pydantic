from pydantic import BaseModel,EmailStr,model_validator
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):

  name : str
  email : EmailStr
  age : int
  weight : float
  married : bool
  allergies : List[str]
  contacts : Dict[str, str]

  @model_validator(mode='after')
  def validate_emergency_contact(cls, model):
     if model.age > 60 and 'emergency' not in model.contacts:
        raise ValueError('Emergency contact is required for patients above 60 years')
     return model
  

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contacts)
    print('updated into db')

patient_info = {'name': 'John','email': 'john@gmail.com', 'age': '65', 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'nuts'], 'contacts': {'phone': '123-456-7890', 'emergency': '987-654-3210'}}

patient1 = Patient(**patient_info) # validation happens here -> type coercion

update_patient_data(patient1)
        