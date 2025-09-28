class student:
    def __init__ (self):
        print()
        print("Student Object is  Created...!")
        print()
    #mutator or setter methods:
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def set_branch(self,branch):
        self.branch=branch
    #acessor or getter methods:
    def get_name(self):
        print(f"Student Name is {self.name}")
    def get_age(self):
        print(f"Student Name is {self.age}")
    def get_branch(self):
        print(f"Student Name is {self.branch}")
s1=student()
s1.set_name("Scott")
s1.set_age(21)
s1.set_branch("ECE")
s1.get_name()
s1.get_age()
s1.get_branch()
    