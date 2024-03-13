var1 = 1
var2 = 2

def someFunc(var1):
    print(f'{var1}, {var2}')

someFunc(3)


def someFunc(func): print(func(5) + 2)

someFunc(lambda x: x * 3)
