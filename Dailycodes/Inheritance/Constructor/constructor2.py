

class Parent:

    def __init__(self):
        print("In Constructor1")

    def __init__(self):
        print("In Constructor2")

Parent()

# op:  In Constructor2 
# the latest construcotr will be consider
