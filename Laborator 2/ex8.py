'''
Write a function that receives a number x, default value equal to 1, a list of strings,
and a boolean flag set to True. For each string, generate a list containing the characters that
have the ASCII code divisible by x if the flag is set to True, otherwise it should contain characters
that have the ASCII code not divisible by x.
'''


def divASCII(x, stringsList, flag):
    newList = []
    for index in stringsList:
        string = []
        for j in index:
            if flag:
                if ord(j) % x == 0:
                    string += j
            else:
                if ord(j) % x == 1:
                    string += j
        if len(string) != 0:
            newList.append(string)
    return newList


if __name__ == '__main__':
    x = 2
    strings = ["test", "hello", "lab002"]
    flag = True
    print(divASCII(x, strings, flag))
