'''
Să se scrie o funcție ce primește ca parametru un string my_path.
Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată descrescător
după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. Lista se obține
din toate fișierele (recursiv) din directorul dat ca parametru.
'''
import os.path


def path(my_path):
    if os.path.isfile(my_path):
        try:
            f = open(my_path)
            s=f.read()
            f.close()
            return s[-20:len(s)]
        except:
            print("Unable to open file")
    else:
        if os.path.isdir(my_path):
            extensionList=[]
            for (root, directories, files) in os.walk("."):
                for fileName in files:
                    fileExtension =os.path.splitext(fileName)
                    if fileExtension[1]!='':
                        extensionList.append(fileExtension[1])
            tupleList=[]
            for i in extensionList:
                if tupleList.count((i,extensionList.count(i)))==0:
                    tupleList.append((i,extensionList.count(i)))
            tupleList.sort(key=lambda a: a[1] ,reverse=True)
            return tupleList

if __name__ == '__main__':
    # print(path("E:\Desktop\An 3 sem 1\Python\Laborator 4\ex3_fisier.txt"))
    print(path("E:\Desktop\An 3 sem 1\Python\Laborator 4"))