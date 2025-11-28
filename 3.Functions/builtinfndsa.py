#palindrome check
'''
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
     '''


#avg of list of integers
'''
nums=[12,3,45,76,4,3,33]
sum=0
for i in nums:
    sum+=i

print (int(sum/len(nums)) )
'''

#sort two list
'''
list1=[1,2,7]
list2=[4,6,5]

mergelist=list1+list2

mergelist.sort();
print(mergelist);
'''

#odd and even tuple   (note:tuple tuple are immutable we cannot create another tuple to insert)
'''
tup=(1,2,3,4,5,6,7,8,9)
tupodd=[]
tupeven=[]

for i in tup:
    if(i%2==0):
        tupeven.append(i)
    else:
        tupodd.append(i)

print(tupodd)
print(tupeven)
'''


#count no of spaces in stiring
'''
strr=input("Enter a string ")
count=0
for i in strr:
    if i==" ":
        count+=1

print("no of spaces are :",count)
'''

#two list share common element
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
set1=set(list1)
set2=set(list2)
if set1.intersection(set2):
    print(" common element ")
else:
    print("common element abset")