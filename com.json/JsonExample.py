import json
from sqlparse.utils import indent

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
x1="hello"
l=[1,2,3]
print(type(x))
# parse x:
y = json.loads(x)
y1=json.dumps(x1)
l1=json.dumps(l,indent=4,separators=(". ", " ="))
print(y)
print(y["name"])
print(y1)
print(type(l))
print(l1)

# the result is a Python dictionary:
# print(y["age"])