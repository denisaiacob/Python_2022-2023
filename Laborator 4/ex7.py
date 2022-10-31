'''
Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si returnează
un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea fisierului in
octeti, file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False daca se poate citi din/scrie in fisier.
'''
import os


def details(path):
    fileDictionary=dict()
    fileDictionary.setdefault("full_path",os.path.abspath(path))
    fileDictionary.setdefault("file_size",os.path.getsize(path))
    fileExtension = os.path.splitext(path)
    fileDictionary.setdefault("file_extension",fileExtension[1])
    fileDictionary.setdefault("can_read",os.access(path,os.R_OK))
    fileDictionary.setdefault("can.write",os.access(path,os.W_OK))
    return fileDictionary

if __name__ == '__main__':
    print(details("E:\Desktop\An 3 sem 1\Python\Laborator 4\ex7_fisier.txt"))