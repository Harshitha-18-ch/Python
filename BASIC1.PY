#1
num1=int(input('Enter the first number:'))
num2=int(input('Enter the second number:'))
print("Summation :",num2+num2)
print(f"Summation :{num2+num2}")


#2
num=int(input("Enter the integer:"))
#if-else
if(num>=-9 and num<=9):
    print("Digit")
else:
    print("Number")
    #temporary operator
res="Digit" if(num>=-9 and num<=9) else "Number"
print(res)


#3
num=int(input("Enter the integer:"))
#if-else
if((num>=10 and num<=99) or (num>=-99 and num<=-10)):
    print("Two Digit NUmber")
else:
    print("Not a Two Digit Number")
    
    
#6
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if(num1>num2):
    print(f"{num1} is largest number")
else:
    print(f"{num2} is largest number")
#ternary operator
res=num1 if(num1>num2) else num2
print(f"{res} is largest number")

    
#8
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if(num1>num2 and num1>num3):
    print(f"{num1} is largest number")
elif(num2>num1 and num2>num3):
    print(f"{num2} is largest number")
else:
    print(f"{num3} is largest number")

#ternary operator
largest=num1 if(num1>num2 and num1>num3)else num2
res=num3 if(num3>num1 and num3>num2) else largest
print(f"{res} is largest number ")


#9
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if(num1<num2 and num1<num3):
    print(f"{num1} is smallest number")
elif(num2<num1 and num2<num3):
    print(f"{num2} is smallest number")
else:
    print(f"{num3} is smallest number")

#ternary operator
smallest=num1 if(num1<num2 and num1<num3)else num2
res=num3 if(num3<num1 and num3<num2) else smallest
print(f"{res} is smallest number ")

