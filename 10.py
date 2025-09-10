
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a > b and a < c) or (a < b and a > c):
    print("a is the middle number")
elif (b > a and b < c) or (b < a and b > c):
    print("b is the middle number")
else:
    print("c is the middle number")