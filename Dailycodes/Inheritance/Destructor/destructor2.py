# class variable and class method

class Parent:
    z = 30

    def __init__(self):
        print("Parent Constructor")
        self.x = 10
        self.y = 20

    def dispData(self):
        print(self.x)
        print(self.y)
    
    # this method will be accesed by [object,Parent] 
    @classmethod
    def parentDisp(cls):
        print(cls.z)

    def __del__(self):
        print("In Destructor")

class Child(Parent):
    pass

obj = Child()
obj.dispData()
obj.parentDisp()
#Parent.parentDisp()

# OP
# Parent Construcotr
# 10
# 20
# 30
# In Destructor


