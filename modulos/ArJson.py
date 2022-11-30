#JSON
import json


js =  '{ "name":"John", "age":30, "city":"New York"}'
#lee el Json
py_js = json.loads(js)
print(py_js['name'])

#diccionario
py ={ "name":"John", 
      "age":30, 
      "city":"New York"
    }
#comvierte de py a json
js_py =json.dumps(py)
print(js_py)


people = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(people, indent=3,separators=(" ", " = "),sort_keys=False)) #false or true
