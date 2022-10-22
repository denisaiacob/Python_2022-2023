'''
 Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters
 in the character string and the values are the number of occurrences of that character in the given text.
'''


def number_of_occurrences(s):
    dictionary = dict()
    for i in s:
        if dictionary.get(i, -1) == -1:
            dictionary.setdefault(i, 1)
        else:
            dictionary.update({i: dictionary[i] + 1})
    return dictionary


if __name__ == '__main__':
    s = "Ana has apples."
    print(number_of_occurrences(s))
