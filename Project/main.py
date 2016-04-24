from MyClass import MyClass

print("Hello world")
obj = MyClass()
while obj.i > 0:
    obj.f()


def inc(a):  # don't work
    a += 1


inc(obj.i)

obj.f()
