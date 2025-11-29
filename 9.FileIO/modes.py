#append
f=open("sample.txt","a")

f.write("new appended text")

f.close()

#x->creates new file and open for writing
f=open("sample2.txt","x")

f.write("new appended text")

f.close()