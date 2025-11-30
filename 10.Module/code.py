import json

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
