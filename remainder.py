hrs=int(input("Enter the last drank hrs:"))
if hrs>=4:
    print("You are dehydrated! Drink water now!")
elif (hrs>=2 and hrs<=3):
    print("Drink a glass of water")
elif hrs<2:
    print("You're fine")