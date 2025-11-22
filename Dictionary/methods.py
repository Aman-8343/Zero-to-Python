
info ={
    "name":"hero",
    "cgpa":10,
    3.14:"pi",
    "subject":["eng","chem"]
}

print(info.keys())
print(type(info.keys()))

print(info.values())

items=info.items()
print(items)   #return all key value pairs


print(info.get("subject"))
print(info.get("subjectsss"))   # return none if no key exists


info.update({
    "city":"djfd"
})
print(info)
