

class Parent:

    def __init__(self):
        print("Parent Constructor")
        print(self)

    def parentFunc(self):
        print("Parent Function")

class Child(Parent):

    def __init__(self):
        print(self)
        #super().__init__()
        Parent()
        print("Child Constructor")

obj1 = Child()
obj1.parentFunc()
