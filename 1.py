import json

person = {
    'name': 'Max',
    'age': 10,
    'phones': ['9111', '738333']
}
a = (1, 3, 5, 7)
result = json.dumps(a)
print(result)
print(type(result))
