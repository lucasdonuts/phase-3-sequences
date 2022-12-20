#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print(list())
        return
    elif length == 1:
        print([0])
        return

    fib = [0, 1]
    i = 2

    while i < length:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
        i += 1

    print(fib)

print_fibonacci(0)
print_fibonacci(1)
print_fibonacci(6)
print_fibonacci(10)