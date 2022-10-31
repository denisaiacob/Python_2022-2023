'''
Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat ca parametru.
Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’ 
'''
import glob
import os


def extension(director):
    extensionList=set()
    fileList=os.listdir(director)
    for i in fileList:
        poz=i.rfind('.')
        if poz!=-1:
            extensionList.add(i[poz+1:len(i)])
    extensionList=list(extensionList)
    extensionList.sort()
    return extensionList

if __name__ == '__main__':
    print(extension("E:\Desktop\An 3 sem 1\Python\Laborator 4"))
