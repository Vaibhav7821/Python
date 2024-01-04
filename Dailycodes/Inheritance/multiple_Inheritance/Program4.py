# mro concept
# in that dfs algo. is used 

class Parent1:
    '''
    def __init__(self):
        print("Parent1 Constructor")
    '''
    pass

class Parent2:
    def __init__(self):
        print("Parent2 Constructor")

class Child(Parent1,Parent2):
    pass
    
obj = Child()

'''
OP:
    Parent2 Constructor
'''

