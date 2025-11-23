#pallindrome check

n=input("Enter a string ");
rev=""

# for i in range(len(n)-1,-1,-1):    #reverse a string using range func
#    rev+=n[i]
   
for i in n:
    rev=i+rev

if n==rev:
     print("palidrome string") 
else:
     print ("not a palindrome")