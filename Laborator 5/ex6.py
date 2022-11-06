'''
Write a function that receives a list with integers as parameter that contains an equal number of even and odd numbers that are in no specific order.
The function should return a list of pairs (tuples of 2 elements) of numbers (Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number
'''


def my_function(myList):
    pairsList = []
    myList.sort(key=lambda i: i % 2)
    h = int(len(myList) / 2)
    for i in range(0, h):
        pairsList.append((myList[i], myList[i + h]))
    return pairsList


if __name__ == "__main__":
    print(my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
