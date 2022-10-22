'''
Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two: reunion, intersection, a-b, b-a.
The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -.
'''


def dictionary_of_operations(setsList):
    d = dict()
    for i in range(0, len(setsList) - 1):
        for j in range(i + 1, len(setsList)):
            key = "" + str(setsList[i]) + "|" + str(setsList[j])
            d.setdefault(key, setsList[i].union(setsList[j]))
            key = "" + str(setsList[i]) + "&" + str(setsList[j])
            d.setdefault(key, setsList[i].intersection(setsList[j]))
            key = "" + str(setsList[i]) + "-" + str(setsList[j])
            d.setdefault(key, setsList[i].difference(setsList[j]))
            key = "" + str(setsList[j]) + "-" + str(setsList[i])
            d.setdefault(key, setsList[j].difference(setsList[i]))
    return d


if __name__ == '__main__':
    setsList = [{1, 2}, {2, 3}]
    print(dictionary_of_operations(setsList))
