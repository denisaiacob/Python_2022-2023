'''
Write a function that receives as a parameter a regex string, a text string and a whole number x,
and returns those long-length x substrings that match the regular expression.
'''
import re
def function(regex,text,x):
    regex=regex+"{"+str(x)+"}"
    result=re.findall(regex,text)
    return result

if __name__ == "__main__":
    print(function("\w","Ana are 2 mere rosii",3))