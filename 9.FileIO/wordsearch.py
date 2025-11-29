data=True
line=1

with open("content.txt","r") as f:
    while data:
        data=f.readline()
        if("python" in data):
            print(f"word found at {line}")
            break
 
        line+=1
   