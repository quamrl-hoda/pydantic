## Pydantic Practice 

This repository contains examples and exercises demonstrating how to use **Pydantic**, a powerful data validation and settings management library for Python. Pydantic helps define Python classes with automatic type checking, data parsing, and validation — making code cleaner, safer, and more reliable.


## About Pydantic
**Pydantic** is built on Python type hints and enforces type validation at runtime. It’s widely used in frameworks like **FastAPI**, **SQLModel**, and **LangChain** to ensure data consistency and correctness.


##  Features
-  Easy data validation with type hints  
-  Automatic type conversion  
-  Clear error messages  
-  Environment variable management  
-  Integrates with FastAPI and other frameworks  

##  Example
from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str
    email: str
user = User(id='1', name='Quamrul', email='quamrul@example.com')
print(user)
### Output:
id=1 name='Quamrul' email='quamrul@example.com'

### Installation
pip install pydantic
### with fastAPI
pip install fastapi[all]

### Project Structure
pydantic/
│
├── 1_padantic_why.py          # Introduction — why we use Pydantic
├── 2_field_validator.py       # Using field validators for data validation
├── 3_model_validator.py       # Model-level validation
├── 4_computed_fields.py       # Working with computed fields
├── 5_nested_models.py         # Nested and complex models
├── 6_serialization.py         # Serialization and parsing examples
│
├── README.md                  # Project documentation
└── tempCodeRunnerFile.py      # Temporary file (VS Code)


### Contributing
Contributions and suggestions are welcome! Fork the repo and create a pull request.
### License
Licensed under the MIT License — free to use and modify.
### Author
🎓 B.Tech | Artificial Intelligence & Machine Learning
