#iii)without using third variable
a=int(input("Enter the value of first integer"))
b=int(input("Enter the value of second integer"))
print(f"a={a}")
print(f"b={b}")
#third logic
a,b=b,a
print("After Swapping:")
print(f"a={a}")
print(f"b={b}")