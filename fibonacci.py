def fibo_1(max):
    a, b, = 0, 1

    while a < max:
        print(a)
        a, b = b, a+b

fibo_1(10)
