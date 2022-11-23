'''
Write another variant of the function from the previous exercise that returns those elements that have at least one
attribute that corresponds to a key-value pair in the dictionary.
'''

import re


def function(path, attrs):
    try:
        f = open(path)
        string = ''
        for line in f:
            string = string + line
        f.close()
    except:
        print("Unable to open file")
    resultList = []
    for key, values in attrs.items():
        result = re.search("(?P<" + key + ">= " + values + ")", string)
    result = re.search(regex, string)
    if result:
        resultList.append(result.group(0))
    return resultList


if __name__ == "__main__":
    attrs = {"class": "url", "name": "url-form"}
    print(function("E:\Desktop\An 3 sem 1\Python\Laborator 6\ex.xml", attrs))
