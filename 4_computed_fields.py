from pydantic import BaseModel,EmailStr,computed_field
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):

  name : str
  email : EmailStr
  age : int
  weight : float # kg
  height : float # mtr
  married : bool
  allergies : List[str]
  contacts : Dict[str, str]

  @computed_field
  @property
  def bmi(self) -> float:
     bmi = self.weight / (self.height ** 2)
     return round(bmi, 2)

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print('BMI:', patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contacts)
    print('updated into db')
    
patient_info = {'name': 'John','email': 'john@gmail.com', 'age': '30', 'weight': 70.5, 'height':1.72, 'married': True, 'allergies': ['pollen', 'nuts'], 'contacts': {'phone': '123-456-7890'}}

patient1 = Patient(**patient_info) # validation happens here -> type coercion

update_patient_data(patient1)