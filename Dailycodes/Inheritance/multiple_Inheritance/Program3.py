

class type:

    def __init__(self,x):
        print("Hello")

class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        print("Child Constructor")
    

obj = Child()

print(type(obj))
'''
    OP: 
        Child Constructor
        Hello
        <__main__.type object at 0x7f7f501cc1f0>

'''
