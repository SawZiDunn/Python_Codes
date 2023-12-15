import json

data = '{"name": "saw", "age": 20, "password": "123"}'

my_api = json.loads(data)

print(my_api)
print(type(my_api))
