num=int(input("Enter the Integer Value:"))
factor=0
pn=num
rev,num=0,0
while(pn!=0):
    rem=pn%10
    rev=rev*10+rem
    pn=pn//10
if(num==rev):
    for i in range(1,num+1):
        if num%i==0:
            factor+=1
res="Prime Palindrome" if(factor==2 and num==rev) else "Not a prime Palindrome"
print(f"{num} is {res}")
 