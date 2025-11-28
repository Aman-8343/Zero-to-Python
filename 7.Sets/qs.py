#list of Tuples
info =[
    ("alice","eng"),
    ("bob","math"),
    ("charlie","math"),
    ("alice","math"),
    ("bob","chem"),
    ("bob","eng")
]


#List all unique course
s=set()
for tup in info:
    s.add(tup[1])
print(s)

#List students enrolled in English
for name,course in info:
    if(course=="eng"):
        print(name)


#create dictionary(students,set of courses)
dict={}
for name,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else :
         dict[name].add(course)

print(dict)