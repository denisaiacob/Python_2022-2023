'''
Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a list with all the vowels in a given string.
'''
import re

vowels = "aAeEiIoOuU"


def my_function(s):
    vowelsList = []
    for i in s:
        if i in vowels:
            vowelsList.append(i)
    return vowelsList


if __name__ == "__main__":
    s = "Programming in Python is fun"
    print(my_function(s))
    vowelsSearch = lambda string: re.findall(f'[{vowels}]', s)
    print(vowelsSearch(s))
    print([i for i in s if i in vowels])
