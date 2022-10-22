'''
Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
The first element of the tuple will be the number of palindrome numbers found in the list and the second element
will be the greatest palindrome number.
'''


def palindrome(numbers):
    max = 0
    nr = 0
    for index in numbers:
        aux = index
        reverse = 0
        while aux > 0:
            c = int(aux % 10)
            reverse = reverse * 10 + c
            aux = int(aux // 10)
        if index == reverse:
            nr = nr + 1
            if index > max:
                max = index
    t = (nr, max)
    return t


if __name__ == '__main__':
    numbers = [121, 23, 1221, 134, 1228, 34543]
    print(palindrome(numbers))
