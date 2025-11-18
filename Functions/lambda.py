#dafault parameter
def average(a,b,c=1):
    ans=int((a+b+c)/3)
    return ans;



avg= average(3,8)
print(avg)
    


sum=lambda a,b,c : a+b+c
print(sum(4,56,5))