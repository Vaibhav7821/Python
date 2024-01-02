def decorFun(func):
    print("In Decor Fun")

    def wrapper():
        print("Start Wrapper1")
        func()
        print("End Wrapper1")

    return wrapper

def decorRun(func):
    print("In Decor Run")

    def wrapper():
        print("Start Wrapper2")
        func()
        print("End Wrapper2")

    return wrapper

@decorFun
@decorRun
def normalFun():
    print("In Normal Fun")


#normalFun = decorFun(decorRun(normalFun))

normalFun()
