'''
 Compare two dictionaries without using the operator "==" returning True or False.
(Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
'''


def compare(d1, d2):
    if len(d1) != len(d2):
        return False

    for i in d1:
        ok = 0
        for j in d2:
            if d1.get(i) == d2.get(j):
                ok = 1
        if ok==0:
            return False

    return True


if __name__ == '__main__':
    d1 = {'A': 1, 'B': 2}
    d2 = {'B': 1, 'A': 1}
    print(compare(d1, d2))
