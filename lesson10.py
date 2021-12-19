import pickle
import json
import yaml
from pydantic import BaseModel
from typing import Optional, Union
import pandas as pd
import openpyxl

#1.Работа с файлом
with open('test.txt', 'w') as f:
   f.write('Тестовая строка')
with open('test.txt','r') as file:
   print (file.read())



# 2.Pickle
d= {'Russia' : 'Moscow',
    'China' : 'Beijing',
    'USA' : 'Washington'}
with open('test_2.txt', 'wb') as f:
    pickle.dump(d, f)
with open('test_2.txt', 'rb') as f:
    d_new = pickle.load(f)
print(d.items())


#3.Сериализация json/yaml
data = {
'age': 45,
'name': 'Peter',
'children': [
{
'age': 3,
'name': 'Alice'
}
],
'married': True,
'city': None
}

#сериализация/десериализация в/из файл(а)
with open('test_3.json', 'w') as f:
    json.dump(data,f)
with open('test_3.json', 'r') as f:
  data_new = json.load(f)

#сериализация/десериализация в/из строки
json_string = json.dumps(data)
data_new = json.loads(json_string)
print(json_string )
print(data_new)

#YAML

f=open('output.yaml','w')
f.write(yaml.dump(data))
f.close


with open('output.yaml', 'r') as f:
    data_new = yaml.safe_load(f)
print(data_new)


#4.use pydantic
class Child(BaseModel):    
    name: str
    age: int

class Person(BaseModel):
    name: str
    age: int
    children: Optional[list[Child]]=None
    married: bool
    city: Union[str,None]
p=Person (**data )
print(p.json())



#xls to csv
df = pd.read_excel('python_test.xlsx')
df.to_csv('output_test.csv', index=False)
