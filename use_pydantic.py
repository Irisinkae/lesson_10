import json
from pydantic import BaseModel
from typing import Optional, Union

class Child(BaseModel):    
    name: str
    age: int

class Person(BaseModel):
    name: str
    age: int
    children: Optional[list[Child]]=None
    married: bool
    city: Union[str,None]

data = {
    'age': 45,
    'name': 'Peter',
    'children': [{
    'name': 'Alice',
    'age': 3
    
}
],
'married': True,
'city': None
}
p=Person (**data )
print(p.json())


