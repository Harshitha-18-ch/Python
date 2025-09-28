class student:
    def __init__ (self,name,age,branch):
        self.StdName=name
        self.Age=age
        self.Branch=branch
S1=student("Scott",20,"CSE")
print(f"Student Name is {S1.StdName}")
print(f"Student Age is {S1.Age}")
print(f"Student Branch is {S1.Branch}")