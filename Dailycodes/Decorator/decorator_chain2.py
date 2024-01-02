def decorFun(func):
    print("In Decor Fun")

    def wrapper(*args):
        print("Start Wrapper1")
        val = func(*args)
        print("End Wrapper1")
        return val 

    return wrapper

def decorRun(func):
    print("In Decor Run")

    def wrapper(*args):
        print("Start Wrapper2")
        val = func(*args)
        print("End Wrapper2")
        return val

    return wrapper

@decorFun
@decorRun
def normalFun(x,y):
    print("In Normal Fun")
    return x+y


#normalFun = decorFun(decorRun(normalFun))

print(normalFun(10,20))
