import json

a = '{"name": ["sajjad", "parvane"], "age": 37, "gender": "male"}'
b = json.loads(a)
print(b)
print(type(a))
print(type(b))
c = json.dumps(b)
print(c)
print(type(json.dumps(31.76)))
d = json.dumps(True)
f = '"true"'
e = 'true'
print(type(json.loads(f)))
print(type(json.loads(e)))


