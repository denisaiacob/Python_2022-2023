'''
Write a function with one parameter which represents a list.
The function will return a new list containing all the numbers found in the given list.
'''
import numbers


def my_function(myList):
    numbersList = []
    for i in myList:
        if isinstance(i, numbers.Number):
            numbersList.append(i)
    return numbersList


if __name__ == "__main__":
    print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
