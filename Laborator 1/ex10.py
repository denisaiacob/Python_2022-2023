def words(string):
    nr = string.split(" ")
    print("Numarul de cuvinte este: %d" % (len(nr)))


if __name__ == "__main__":
    string = input("Dati un text\n")
    words(string)
