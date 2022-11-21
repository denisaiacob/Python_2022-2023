'''
Write a function that recursively scrolls a directory and displays those files whose name matches a regular expression given as a
parameter or contains a string that matches the same expression. Files that satisfy both conditions will be prefixed with ">>"
'''
import os
import re


def function(regex):
    for (root, directories, files) in os.walk("."):
        for fileName in files:
            matches = 0
            if re.match(regex, fileName):
                matches = matches + 1
            ok = False
            try:
                f = open(fileName)
                for line in f:
                    if re.match(regex, line):
                        ok = True
                f.close()
            except:
                print("Unable to open file")
            if matches == 1:
                if ok == True:
                    print(">>" + fileName)
                else:
                    print(fileName)


if __name__ == "__main__":
    function("\w+")
