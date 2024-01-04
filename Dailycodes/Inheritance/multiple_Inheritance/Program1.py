# basic inheritance 

class Parent1:

    def dispData(self):
        print("In dispData")

class Parent2:
    def printData(self):
        print("In printData")

class Child(Parent1,Parent2):
    pass

obj = Child()
obj.dispData()
obj.printData()
