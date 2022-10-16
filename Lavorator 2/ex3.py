def intersection(a, b):
    intersection_list = a.intersection(b)
    return list(intersection_list)


def union(a, b):
    union_list = a.union(b)
    return list(union_list)


def a_minus_b(a, b):
    minus_list = a.symmetric_difference(intersection(a, b))
    return list(minus_list)


def b_minus_a(a, b):
    minus_list = b.symmetric_difference(intersection(a, b))
    return list(minus_list)


if __name__ == '__main__':
    a = [1, 'a', 7, 8, 'c']
    b = [1, 'b', 7, 9, 'c']
    a = set(a)
    b = set(b)
    print(intersection(a, b))
    print(union(a, b))
    print(a_minus_b(a, b))
    print(b_minus_a(a,b))
