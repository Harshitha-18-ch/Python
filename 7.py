num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if(num1<num2):
    print(f"{num1} is smallest number")
else:
    print(f"{num2} is smallest number")
#ternary operator
res=num1 if(num1<num2) else num2
print(f"{res} is smallest number")