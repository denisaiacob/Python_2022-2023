'''
Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la linia de comandă (nerecursiv).
Lista trebuie să fie sortată crescător.
Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală.
'''
import os


def extension(path):
    fileList = os.listdir(path)
    extensionList = set()
    for i in fileList:
        poz = i.rfind('.')
        if poz != -1:
            extensionList.add(i[poz + 1:len(i)])
    extensionList = list(extensionList)
    extensionList.sort()
    return extensionList


if __name__ == '__main__':
    path = input("Dati calea directorului:")
    print(extension(path))
