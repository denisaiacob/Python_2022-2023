'''
 Write a function that receives a variable number of arguments and keyword arguments.
 The function returns a list containing only the arguments which are dictionaries, containing minimum 2 keys and at
 least one string key with minimum 3 characters.
'''


def max_key(d):
    maxc = 0
    for j in d.keys():
        if isinstance(j, str):
            if len(j) > maxc:
                maxc = len(j)
    return maxc


def my_function(*args, **kwargs):
    dictionariesList = []
    for i in args:
        if isinstance(i, dict):
            dictionariesList.append(i)
    for i in kwargs.values():
        if isinstance(i, dict):
            dictionariesList.append(i)
    dictionariesList = [i for i in dictionariesList if len(i) >= 2 and max_key(i) >= 3]
    return dictionariesList


if __name__ == "__main__":
    print(my_function({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
                      dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))
