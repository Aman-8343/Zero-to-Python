
try:
    n=int(input("Enter no."))
    ans=10/n
    
except ZeroDivisionError:
    print("no in not divisible by 0")
except ValueError:
    print("invalid input")
else :
    print(f"ans is {ans}")