def fibo_1(max):
    a, b, = 0, 1

    while a < max:
        print(a)
        a, b = b, a+b

def fibo_3(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

fibo_1(10)
for n in fibo_3(10):
    print(n)
