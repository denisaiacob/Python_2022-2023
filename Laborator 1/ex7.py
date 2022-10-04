def number(string):
    nr = 0
    for index in range(0, len(string)):
        if string[index].isnumeric():
            i = 0
            while string[index + i].isnumeric():
                nr = nr * 10 + (int)(string[index + i])
                i = i + 1
            break
    print(nr)


if __name__ == "__main__":
    string = input("Dati un text\n")
    number(string)
