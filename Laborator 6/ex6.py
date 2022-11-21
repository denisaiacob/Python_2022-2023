'''
Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
Censorship means replacing characters from odd positions with *.
'''
import re


def censorship(text):
    words = re.findall("[aeiouAEIOU]\w*[aeiouAEIOU]", text)
    for w in words:
        newWord = ''
        for i in range(0, len(w)):
            if i % 2 == 1:
                newWord = newWord + '*'
            else:
                newWord = newWord + w[i]
        text = re.sub(w, newWord, text)

    return text


if __name__ == "__main__":
    print(censorship("abca cda Eaaaei ann"))
