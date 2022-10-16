'''
 Write a function that will receive a list of words  as parameter and will return a list of lists of words,
grouped by rhyme.Two words rhyme if both of them end with the same 2 letters.
'''


def group_by_rhyme(wordsList):
    wordsList.sort(key=lambda i: i[-2:len(i)])
    sortList=[]
    i = 0
    while i < len(wordsList):
        j = i + 1
        newList=[wordsList[i]]
        while j < len(wordsList) and wordsList[i][-2:len(wordsList[i])] == wordsList[j][-2:len(wordsList[j])]:
            newList.append(wordsList[j])
            j = j + 1
        sortList.append(newList)
        i = j

    return sortList


if __name__ == '__main__':
    wordsList = ['ana', 'banana', 'carte', 'arme', 'parte']
    print(group_by_rhyme(wordsList))