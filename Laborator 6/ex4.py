'''
Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns those elements
that have as attributes all the keys in the dictionary and values the corresponding values.
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
    regex = ''
    for key, values in attrs.items():
        regex = regex + "(?P<" + key + ">= " + values + ")"
    result = re.search(regex, string)
    if result:
        return result.groupdict()


if __name__ == "__main__":
    attrs = {"class": "url", "name": "url-form"}
    print(function("E:\Desktop\An 3 sem 1\Python\Laborator 6\ex.xml", attrs))
