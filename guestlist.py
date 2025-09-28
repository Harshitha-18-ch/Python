Guest_List=[]
while(True):
    print("______Guest List Menu__________")
    print("1.To view the Guest LIit")
    print("2.To Add a Guest")
    print("3.Check")
    print("4.To Remove a Guest")
    print("5.print Finalized guest ")
    choice=int(input("Enter Your choice:"))
    if choice==1:
        if(len(Guest_List)==0):
            print("Guest List is Empty")
        else:
            print("Guest List:")
            print(Guest_List)
        print()
    elif(choice==2):
        guest=input("Enter the Guest Name:")
        Guest_List.append(guest)
        print(f"{guest} is added to the guest list....!")
        print()
    elif(choice==3):
        guest=input("Enter the guest name to check the status")
        if guest in Guest_List:
            print(f"{guest} is attending party...!")
        else:
            print(f"{guest} is Not Attending the party...!")
        print()
    elif(choice==4):
        guest=input("Enter the nE OF THE GUEST WHO's not")
        if guest in Guest_List:
            Guest_List.remove(guest)
        print()
    elif(choice==5):
        print("Finalized Guest List:")
        print()
        print(Guest_List)
    break