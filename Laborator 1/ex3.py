if __name__ == "__main__":
    string1 = input("Scrie primul sir\n")
    string2 = input("Scrie al doilea sir\n")
    nr = len(string2.split(string1)) - 1
    print("Numarul de aparitii ale primului sir in cel de al doilea este: %d" % (nr))
