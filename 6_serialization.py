from pydantic import BaseModel

class Address(BaseModel):
  city : str
  state : str
  pin : str

class Patient(BaseModel):
  name : str
  gender : str = 'Male'
  age : int
  address : Address

address_dict = {'city': 'purnia', 'state': 'Bihar', 'pin': '854302'}

address1 = Address(**address_dict)

patient_dict = {'name': 'quamrul','age':'21', 'address': address1}
patient1 = Patient(**patient_dict)

temp = patient1.model_dump()
temp1 = patient1.model_dump_json()
temp2 = patient1.model_dump(include=['name', 'age'])
temp3 = patient1.model_dump(exclude=['name', 'age'])
temp4 = patient1.model_dump(exclude=['address', 'state'])
temp5 = patient1.model_dump(exclude_unset=True)



print(temp)
print(type(temp))
print(temp1)
print(type(temp1))
print(temp2)
print(type(temp2))
print(temp3)
print(type(temp3))
print(temp4)
print(type(temp4))
print(temp5)
print(type(temp5))