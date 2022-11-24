'''
Write a function that receives two parameters: a list of strings and a list of regular expressions. The function will return
a list of the strings that match on at least one regular expression from the list given as parameter.
'''
import re


def function(text, regexList):
    stringsList = set()
    for t in text:
        ok = False
        for r in regexList:
            if re.match(r + "$", t):
                ok = True
        if ok == True:
            stringsList.add(t)
    stringsList = list(stringsList)
    return stringsList


if __name__ == "__main__":
    regexList = ["\d+", "[0-9]{3}"]
    text = ["Exemplu", "123", "15aa", "aa15"]
    print(function(text, regexList))
