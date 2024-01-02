
class Demo:

    def __init__(self):
        print("Constructor")
    
    def __del__(self):
        print("Destructor")

obj1 = Demo()
obj2 = Demo()

obj3 = obj1
del obj1
print("End Code")


# OP :
# Constructor
# Constructor
# End Code
# Destructor
# Destructor
