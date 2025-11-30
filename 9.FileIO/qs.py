'''
f=open("names2.txt","w")
f.write("Aman\n")
f.write("Anuj\n")
f.write("Ankit\n")  
f.write("Ashish\n")
f.write("Aditya\n")

f.close()

f=open("names2.txt","r")
content=f.read()
print(content)
'''

'''
with open("log.txt", "a") as f:
    f.write("new logs")

with open("log.txt","r") as f:
    content = f.read()

print(content)
'''