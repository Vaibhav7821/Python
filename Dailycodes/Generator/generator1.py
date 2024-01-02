
def fun():
    yield 10
    yield 20

ret = fun()

print(next(ret))
print(next(ret))
print(next(ret))
