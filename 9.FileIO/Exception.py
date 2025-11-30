
try:
    n=int(input("Enter no."))
    ans=10/n
    
except ZeroDivisionError:
    print("no in not divisible by 0")
except ValueError:
    print("invalid input")
else :
    print(f"ans is {ans}")

finally:     #always execute
    print("end of code")




try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("File not found!")
