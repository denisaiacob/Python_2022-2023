def fibonacci(n):
    fib = []
    for index in range(0, n):
        if index == 0:
            fib += [0]
        elif index == 1:
            fib += [1]
        else:
            fib += [fib[index - 1] + fib[index - 2]]
    return fib


if __name__ == '__main__':
    print(fibonacci(15))
