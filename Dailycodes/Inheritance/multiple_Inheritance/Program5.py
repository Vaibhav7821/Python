

class A:
    def fun(self):
        print("In fun A")

class B:
    def fun(self):
        print("In fun B")

class C:
    def fun(self):
        print("In fun C")

class D(A,B):
    def fun(self):
        print("In fun D")
        super().fun()

class E(B,C):
    def fun(self):
        print("In fun E")
        super().fun()

class F(D,E):
    def fun(self):
        print("In fun F")
        super().fun()

obj = F()
obj.fun()
print(F.mro())


'''
    OP :
        In fun F
        In fun D
        In fun A
        [<class '__main__.F'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

'''
