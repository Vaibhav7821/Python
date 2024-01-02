

def decorFun(func):
    print("In Decor Fun")

    def wrapper():
        print("Start Wrapper")
        func()
        print("End Wrapper")

    return wrapper
@decorFun
def normalFun():
    print("In Normal Fun")

#normalFun = decorFun(normalFun)
normalFun()
