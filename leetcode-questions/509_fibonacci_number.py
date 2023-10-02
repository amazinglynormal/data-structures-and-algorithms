def fib_recursive(n: int) -> int:
    if n <= 1:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    if n == 1:
        return n

    result = 0
    i = 0
    j = 1
    for _ in range(n - 1):
        result = i + j
        i = j
        j = result

    return result


print(fib_recursive(2))  # 1
print(fib_recursive(3))  # 2
print(fib_recursive(6))  # 8

print(fib_iterative(2))  # 1
print(fib_iterative(3))  # 2
print(fib_iterative(6))  # 8
