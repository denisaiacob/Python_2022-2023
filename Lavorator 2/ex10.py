'''
Write a function that receives a variable number of lists and returns a list of tuples as follows:
the first tuple contains the first items in the lists,
the second element contains the items on the position 2 in the lists, etc.
Note: If input lists do not have the same number of items, missing items will be replaced with None
to be able to generate max ([len(x) for x in input_lists]) tuples.
'''


def sort_tuple(lists):
    m = max(len(x) for x in lists)
    for index in lists:
        if len(index) < m:
            for j in range(m - len(index)):
                index.append(None)
    newList = []
    for i in range(0, m):
        t = ()
        for j in range(0,len(lists)):
            t = t + (lists[j][i],)
        newList.append(t)
    return newList


if __name__ == '__main__':
    lists = [[1, 2, 3], [5, 6, 7], ["a", "b", "c"], [8]]
    print(sort_tuple(lists))
