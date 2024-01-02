

class Parent:

    def __init__(self):
        print("Parent Constructor")

    def __del__(self):
        print("In Destructor")

obj = Parent()
obj = Parent()

print("Code Samplay")

# OP:
# Parent Constructor
# Parent Constructor
# In Destructor
# Code Samplay
# In Destructor

