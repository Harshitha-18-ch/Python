n=int(input("Enter the integer"))
print(f"Even numbers from {n} to 1")
for i in range(n,1,-1):
    if i%2==0:
        print(i)