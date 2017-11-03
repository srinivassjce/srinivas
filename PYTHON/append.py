def foo(i, x=[]):
    x.extend([ x.extend(i)])
    return x
for i in range(3):
    y = foo([i])
print(y)
