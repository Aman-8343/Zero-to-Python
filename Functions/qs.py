# salary=int(input("enter no "))
# if(salary<3000):
#     print("5% tax")
# elif(salary>=3000 and salary<7000):
#     print("15 % tax") 
# else: 
#     print("25% tax")       



#even no from a to b
# def even_no(a,b):
#     for i in range(a,b+1):
#         if(i%2==0):
#             print(i)

# print(even_no(3,40))

#count number of digits
def func(n):
    count=0
    while(n>0):
        count+=1
        n//=10
    return count
           
    
print(func(0))    
