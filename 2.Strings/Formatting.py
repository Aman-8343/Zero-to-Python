a=5
b=7
sum=a+b;

#normal formatting
print("lang is {}".format("python"))
print("sum is {}".format(sum))
print("sum of {} and {} is {}".format(a,b,sum))

#index based formatting

print("sum of {1} and {0} is {2}".format(a,b,sum))

#value based formatting
print("val of {a} and {b}".format(a=5,b=7))

#F strings
d=5
e=6
print(f"sum of {d} and {e} is {d+e}")