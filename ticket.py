Age=int(input("Enter the Age:"))
if Age<12:
    print("Rs.150")
elif Age>=12 and Age<=18:
    print("Rs.200")
elif Age>18:
    print("Rs.300")
else:
    print("Invalid Age")