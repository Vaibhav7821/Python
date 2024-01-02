

class Demo :

    def __init__(self):
        print("Constructor")
        self.x = 10
        self.y = 20

    def setData(self,x):
        self.z = x

    def printData(self):
        print(self.x)
        print(self.y)
        print(self.z)

obj1 = Demo()
obj1.setData(30)
obj1.printData()

