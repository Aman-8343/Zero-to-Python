ans= [i*i for i in range(6) if i%2!=0]
print (ans)


res=[-2,-4,4,6,-4,8]
a=[0 if val<0 else val for val in res]
print(a)


nums=[5,10,15,20,34,36]
s=[val for val in nums if val>15]
print(s)