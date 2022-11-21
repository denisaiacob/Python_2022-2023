'''
Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters.
'''
import re

def words_function(text):
    words=re.findall("\w+", text)
    return words
if __name__ == "__main__":
    print(words_function("Text abbc 13ab,b14."))