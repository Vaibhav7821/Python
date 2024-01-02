

class Parent:

    def __init__(self):
        print("In parent Constrcutor")

    def parentFun(self):
        print("Parent Function")

class Child(Parent):

    def __init__(self):
        print("In child Constrcutor")
   

obj1 = Child()
obj1.parentFun()

# OP:
# In child Construcotr
# Parent Function

# Parent construtor will be comes in the child if there is no construcotr present of child 
# if present then it will be considered the Childs constructor not parent
