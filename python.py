def sqrt(n):
    x = 0
    while x*x <= n:
        x += 1
    return x-1

print(sqrt(16))
