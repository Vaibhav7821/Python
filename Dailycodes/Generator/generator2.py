

def fun():
    print("Start Fun")
    yield 10
    yield 20
    yield 30
    print("End Fun")
    yield 

print(fun);
ret = fun()
print(ret)
print(next(ret))
print(next(ret))
print(next(ret))
next(ret)
print(fun);

