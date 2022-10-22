'''
Write a function that receives as parameters two lists a and b and returns a list of sets containing:
(a intersected with b, a reunited with b, a - b, b - a)
'''


def list_processing(a, b):
    a = set(a)
    b = set(b)
    setsList = []
    setsList.append(a.intersection(b))
    setsList.append(a.union(b))
    setsList.append(a.difference(b))
    setsList.append(b.difference(a))
    return setsList


if __name__ == '__main__':
    a = [1, 'a', 7, 8, 'c']
    b = [1, 'b', 7, 9, 'c']
    print(list_processing(a, b))
