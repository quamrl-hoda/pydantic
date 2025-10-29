from pydantic import BaseModel, ValidationError,Field,EmailStr,field_validator
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):

  name : str
  email : EmailStr
  age : int
  weight : float
  married : bool
  allergies : List[str]
  contacts : Dict[str, str]

  @field_validator('email')
  @classmethod
  def validate_email(cls, value):

     valid_domain = ['hdfc.com', 'icici.com', 'gmail.com']
     #abc@gmail.com
     domain_name = value.split('@')[-1]
     if domain_name not in valid_domain:
        raise ValueError('Email domain is not valid')
     return value
  
  @field_validator('name')
  @classmethod
  def transform_name(cls, value):
     return value.upper()
  
  @field_validator('age', mode='after')
  @classmethod
  def validate_age(cls, value):
     if 0 < value < 100:
        return value
     raise ValueError('Age must be between 1 and 99')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contacts)
    print('updated into db')

patient_info = {'name': 'John','email': 'john@gmail.com', 'age': '30', 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'nuts'], 'contacts': {'phone': '123-456-7890'}}

patient1 = Patient(**patient_info) # validation happens here -> type coercion

update_patient_data(patient1)
