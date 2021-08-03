def fib(n):
    if n<2:
        return n
    current, next = 0, 1
    while n:
        current, next = next ,current + next
        n -= 1
        print(current)
    return current


fib(12)
