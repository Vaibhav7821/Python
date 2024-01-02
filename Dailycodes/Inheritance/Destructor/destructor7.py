

class Demo:

    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("Destructor")

def fun():
    print("Start Fun")
    obj = Demo()
    print("End Fun")

def gun():
    print("Start Gun")
    obj = Demo()
    print("End Gun")
    return obj

print("Start Code")
fun()
ret = gun()
print("End Code")

# OP :
# Start Code
# Start Fun
# Constructor
# End Fun
# Destructor
# Start Gun
# Constructor
# End Gun
# End Code
# Destructor
