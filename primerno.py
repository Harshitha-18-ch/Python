num=int(input("Enter the Integer value:"))
factor=0
for i in range(1,num+1):
    if(num%i==0):
        factor+=1
res="Prime Number" if(factor==2) else "Not a Prime Number"
print(f"{num} is {res}")
