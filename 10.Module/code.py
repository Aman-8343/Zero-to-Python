import json

'''
py_dict={
    "name":"hero",
    "ishero":"true"
}

json_str='{"name":"aman","isbo":true}'

py_obj= json.loads(json_str)   #convert json string to python dict

strr= json.dumps(py_dict)   #convert python dict to json string

print(py_obj)
print(type(py_obj))

print(strr,type(strr))
'''


#dealing with files

with open("data.json","r") as f:
     obj=json.load(f)
     print(obj)
     print(type(obj))