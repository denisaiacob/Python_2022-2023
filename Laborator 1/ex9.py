def mostCommonCharacter(string):
    string = string.lower()
    max = -1
    for index in string:
        if index.isalpha() and string.count(index) > max:
            max = string.count(index)
            character = index
    print(character)


if __name__ == "__main__":
    string = input("Dati un text\n")
    mostCommonCharacter(string)
