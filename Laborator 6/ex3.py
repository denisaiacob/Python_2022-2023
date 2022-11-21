'''
Write a function that receives as a parameter a string of text characters and a list of regular expressions and returns
a list of strings that match on at least one regular expression given as a parameter.
'''
import re


def function(text, regexList):
    stringsList = set()
    for r in regexList:
        result = re.findall(r, text)
        for i in result:
            stringsList.add(i)
    stringsList = list(stringsList)
    return stringsList


if __name__ == "__main__":
    regexList = ["\w+", "\d+", "[0-9]{3}"]
    print(function("Exemplu 123 ", regexList))
