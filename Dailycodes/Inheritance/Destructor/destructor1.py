
class Demo:

    def __init__(self):
        print("Constructor")

    def dispData(self):
        print("Disp Data")

    def __del__(self):
        print("Destructor")

obj = Demo()
obj.dispData()
del obj
# obj.__del__()

# OP:
# Constructor
# Disp Data
# Destructor
