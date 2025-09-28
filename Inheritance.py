class Person:
    def __init__(self,Name,Age,Branch):
        print('Person Object is Created...!')
        self.Name=Name
        self.Age=Age
        self.Branch=Branch
class student(Person):
    def __init__ (self,Name,Age,Gender,Id,Branch):
        super().__init__ (Name,Age,Gender)
        self.Id=Id
        self.Branch=Branch
        print("Student Object is Created..!")
s1=student(1,2,3,4,5)