def countBits(number):
    binary = format(number, "b")
    print(binary)
    nr = 0
    for index in binary:
        if (int)(index) == 1:
            nr = nr + 1
    print(nr)


if __name__ == "__main__":
    number = input("Dati un numar\n")
    countBits((int)(number))
