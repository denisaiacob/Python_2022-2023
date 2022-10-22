'''
 Write a function that receives as a parameter a variable number of lists and a whole number x.
 Return a list containing the items that appear exactly x times in the incoming lists.
'''


def aparitions(lists, x):
    listsUnion = []
    for index in range(0, len(lists)):
        listsUnion += lists[index]
    newList = list({i for i in listsUnion if listsUnion.count(i) == x})
    return newList


if __name__ == '__main__':
    lists = [[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]]
    x = 2
    print(aparitions(lists, x))
