bill=int(input("Enter the bill:"))
if bill>100:
    discount=(10/100)*bill
    fin_acc=bill-discount
    print(f"Final Amount {fin_acc}")
elif bill>500:
    discount=(5/100)*bill
    fin_acc=bill-discount
    print(f"Final Amount {fin_acc}")
elif bill<=500:
    print("No Discount")
