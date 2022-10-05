def fibonacci(n):
    if n == 0:
        return 1
    elif  n == 1:
        return 1
    else:                                        # n >= 2 인 경우
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(10):
    print(fibonacci(n), end=', ')

print('...')
print(fibonacci(10))
