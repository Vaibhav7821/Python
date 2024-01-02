

class Demo :
    z = 30          #  without any underscore(_) is public in python

    def __init__(self):
        self._x = 10;      # single enderscore(_) is protected in python
        self.__y = 20;       # double enderscore(__) is private in python

obj = Demo()
print(obj.z)        # 30
print(obj._x)       # 10
#print(obj.__y)  # attribute error : attribute __y is not defind
                # pyhton stores private internally as == _Demo__y
                # now it can accessed by using that name 
                # python done name mangling of private variable

print(obj._Demo__y) # 20

