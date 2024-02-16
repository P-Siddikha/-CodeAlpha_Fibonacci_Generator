def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y =  y, x + y


n = int(input("Input the number of Fibonacci numbers you want to generate? "))

print("Number of first ",n,"Fibonacci numbers:")
fib = fibonacci()
for _ in range(n):
    print(next(fib),end= " ")