amount=int(input("Enter the amount:"))
acc_balance=5000
if(amount<=acc_balance and amount%100==0):
    print("Withdrawl Successful")
else:
    print("Insufficient Balance")