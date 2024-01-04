# basic inheritance with constructor

class Parent1:
    '''
    def __init__(self):
        print("In Constructor: Parent1")
   ''' 
    def dispData(self):
        print("In dispData")

class Parent2:
    '''
    def __init__(self):
        print("In Constructor: Parent2")
    '''
    def printData(self):
        print("In printData")

class Parent3:
    def __init__(self):
        print("In Constructor: Parent3")

class Child(Parent1,Parent2,Parent3):     # left side preference is taken here
    pass

obj = Child()
obj.dispData()
obj.printData()

''' 
OP :
    In Constructor: Parent3
    In dispData
    In printData
'''
