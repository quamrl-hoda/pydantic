from pydantic import BaseModel, ValidationError, conint, EmailStr,AnyUrl,Field
from typing import List, Dict, Optional,Annotated


class Patient(BaseModel):
    
    name: Annotated[str, Field(min_length=1, max_length=100,title="Patient Name", description="Name must be between 1 and 100 characters", example="John Doe")]
    email: Annotated[EmailStr, Field(description="Email must be a valid email address")]
    linkedin_url: Optional[Annotated[AnyUrl, Field(description="LinkedIn URL must be a valid URL")]] = None
    age: Annotated[int, Field(ge=0, le=120, description="Age must be between 0 and 120")]
    weight: Annotated[float, Field(gt=0, strict=True,description="Weight must be greater than zero")]
    married: Annotated[bool, Field(default=None, description="Marital status of the patient")]
    allergies: Optional[Annotated[List[str], Field(max_items=10, default_factory=list)]]
    contacts: Annotated[Dict[str, str], Field(description="Contact information of the patient")]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contacts)
    print('inserted into db')

 
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated into db')

patient_info = {'name': 'John','email': 'john@example.com', 'age': 30, 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'nuts'], 'contacts': {'phone': '123-456-7890'}}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)

# # Without Pydantic
# def insert_patient_data(name, age):
#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)
#         print('inserted into db')
#     else:
#         raise TypeError('Invalid data types for name or age')
     
# def update_patient_data(name:str, age:int):
#      if type(name) == str and type(age) == int:
#          print(name)
#          print(age)
#          print('updated into db')
#      else:
#           raise TypeError('Invalid data types for name or age')
# insert_patient_data('John', 30)