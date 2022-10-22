'''
Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique elements in the list,
and b representing the number of duplicate elements in the list (use sets to achieve this objective).
'''
def number_of_elements(elementsList):
    dictionary = dict()
    for i in elementsList:
        if dictionary.get(i, -1) == -1:
            dictionary.setdefault(i, 1)
        else:
            dictionary.update({i: dictionary[i] + 1})
    duplicate=0
    unique=0
    for i in dictionary:
        if dictionary.get(i)>1:
            duplicate=duplicate+1
        else:
            unique=unique+1
    return (unique,duplicate)

if __name__ == '__main__':
    elementsList=[1,2,3,1,1,2,4,5]
    print(number_of_elements(elementsList))