
class Parent :

    def __init__(self):
        print("Parent COnstructor")

    def parentFunc(self):
        print("Parent Function")

class Child(Parent):
    
    def __init__(self):
        # these are thr threee ways of calling parent constrcutor from child construcotr
        super().__init__()
        Parent.__init__(self)
        Parent()
        print("Child COnstructor")

obj = Child()
obj.parentFunc()

