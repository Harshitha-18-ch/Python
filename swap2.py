#i)using third variable
a=int(input("Enter the value of first integer"))
b=int(input("Enter the value of second integer"))
print(f"a={a}")
print(f"b={b}")
#second logic
temp=a
a=b
b=temp
print("After Swapping:")
print(f"a={a}")
print(f"b={b}")