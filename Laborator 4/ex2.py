'''
Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a
fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.
'''
import os.path


def path(director,fisier):
    try:
        f=open(fisier,wt)
        fileList = os.listdir(director)
        for i in fileList:
            if i[0]=='A':
                f.write(os.path.abspath(fileList))
        f.close()
    except:
        print("Unable to open file")



if __name__ == '__main__':
    path("E:\Downloads","E:\Desktop\An 3 sem 1\Python\Laborator 4\ex2_fisier.txt")