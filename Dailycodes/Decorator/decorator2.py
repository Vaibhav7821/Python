

def decorFun(func):

    print("In Decor Fun")

    def wrapper(*args):

        print("Start Wrapper")
        val = func(*args)
        print("End Wrapper")
        return val
    return wrapper


@decorFun
def normalFun(x,y):
    print("In Normal Fun")
    return x+y

print(normalFun(10,20))
