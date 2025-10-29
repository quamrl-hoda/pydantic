# Pydantic Practice 🚀

This repository contains examples and exercises demonstrating how to use **Pydantic**, a powerful data validation and settings management library for Python. Pydantic helps define Python classes with automatic type checking, data parsing, and validation — making code cleaner, safer, and more reliable.

---

## About Pydantic
**Pydantic** is built on Python type hints and enforces type validation at runtime. It’s widely used in frameworks like **FastAPI**, **SQLModel**, and **LangChain** to ensure data consistency and correctness.

---

##  Features
-  Easy data validation with type hints  
-  Automatic type conversion  
-  Clear error messages  
-  Environment variable management  
-  Integrates with FastAPI and other frameworks  

---

##  Example
```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

user = User(id='1', name='Quamrul', email='quamrul@example.com')
print(user)
