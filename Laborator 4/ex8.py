'''Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un director aflat pe disc.
Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.
'''
import os


def absolute_path(dir_path):
    pathList = []
    fileList = os.listdir(dir_path)
    for fileName in fileList:
        if os.path.isfile(fileName):
            pathList.append(os.path.abspath(fileName))
    return pathList


if __name__ == '__main__':
    print(absolute_path("E:\Desktop\An 3 sem 1\Python\Laborator 4"))
