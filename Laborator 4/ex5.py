'''
Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza o listă de
fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in fișierul
respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director.
Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
'''
import os


def search(target, to_search):
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
    except ValueError:
        print('ValueError')
    except:
        print("Unable to open file")


if __name__ == '__main__':
    print(search("E:\Desktop\An 3 sem 1\Python\Laborator 4", "0"))
