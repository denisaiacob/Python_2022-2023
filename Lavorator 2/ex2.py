def is_prime(n):
    if n > 1:
        d = int(n / 2)
        for i in range(2, d + 1):
            if n % i == 0:
                return 0
        return 1


def prime_numbers_list(l):
    prime = []
    for index in l:
        if is_prime(index):
            prime += [index]
    return prime


if __name__ == '__main__':
    x = [9, 2, 1, 4, 13, 6, 24, 7]
    print(prime_numbers_list(x))
