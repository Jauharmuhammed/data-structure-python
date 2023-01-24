
# using generators
def fib(limit):
    a, b = 0, 1

    while a < limit:
        yield a
        a, b = b, a+b


for i in fib(5):
    print(i)


# using for loop
def fibonacci(limit):
    fib = [0, 1]

    for i in range(2, limit):
        fib.append(fib[i-1] + fib[i-2])

    return fib

print(fibonacci(5))