string=input("Enter the String:")
alphabet,digit,specialchar=0,0,0
for ch in string:
    if ch.isalpha():
        alphabet+=1
    elif ch.isdigit():
        digit+=1
    else:
        specialchar+=1
print(f"Count of Alphabetic characters is {alphabet}")
print(f"Count of Digits is {digit}")
print(f"Count of Special characters is {specialchar}")