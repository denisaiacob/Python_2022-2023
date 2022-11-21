'''
Verify using a regular expression whether a string is a valid CNP.
'''
import re


def isCNP(string):
    if re.match("^[1-9]{1}[0-9]{12}$", string):
        return True
    else:
        return False


if __name__ == "__main__":
    print(isCNP("5010612121214"))
