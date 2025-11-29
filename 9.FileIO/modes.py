#append
'''
f=open("sample.txt","a")

f.write("new appended text")

f.close()
'''

#x->creates new file and open for writing
'''
f=open("sample2.txt","x")

f.write("new appended text")

f.close()
'''

# + -> open disk file for both reading and writing
f=open("sample.txt","r+")
f.write("writing new text")
content=f.read()
print(content)