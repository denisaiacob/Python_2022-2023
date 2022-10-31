'''
Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește un
parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în procesarea
fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru.
'''

import os

def callbackFunc(e):
    print('Exceptia este: ', e)

def search(target, to_search,callback):
    try:
        fileList = []
        if os.path.isfile(target):
            f = open(target, r)
            s = f.read()
            if s.find(to_search) != -1:
                fileList.append(os.path.basename(target))
            f.close()
        else:
            if os.path.isdir(target):
                for (root, directories, files) in os.walk("."):
                    for fileName in files:
                        full_fileName = os.path.join(root, fileName)
                        f = open(full_fileName, r)
                        s = f.read()
                        if s.find(to_search) != -1:
                            fileList.append(os.path.basename(target))
                        f.close()
        return fileList
    except ValueError as e:
        callback(e)
    except Exception as e:
        callback(e)


if __name__ == '__main__':
    print(search("E:\Desktop\An 3 sem 1\Python\Laborator 4", "0",callbackFunc))
