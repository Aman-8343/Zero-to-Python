nums=[1,2,4,6,8]
x=6
idx=0

for val in nums:    
    if(val==x):
        print(f"{x} found at index {idx}")
        break
    else: idx+=1

