#arithmetic  operations
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
while(True):
    print("______________Operations Menu____________")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        print(f"Summation of {a},{b} is {a+b}")
        print()
    elif(choice==2):
        print(f"Difference of {a},{b} is {a-b}")
        print()
    elif(choice==3):
        print(f"Product of {a},{b} is {a*b}")
        print()
    elif(choice==4):
        print(f"Quotient of {a},{b} is {a/b}")
        print()
    elif(choice==5):
        print("Thanks for using the Operations Menu")
    break