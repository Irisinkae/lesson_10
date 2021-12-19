import json

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