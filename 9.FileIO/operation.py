'''
f=open("data.txt","w")

f.write("overwrittten text")

f.close()
'''

#with - open file and automatically close after block

with open("sample.txt","r") as f:
    data=f.read()
    print(data)
    print(len(data))

