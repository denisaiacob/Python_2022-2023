if __name__ == "__main__":
    string = input("Scrie stringul\n")
    for index in range(0, len(string)):
        if string[index].isupper():
            if (index != 0):
                string = string[0:index] + "_" + string[index].lower() + string[index + 1:len(string)]
            else:
                string = string[0:index] + string[index].lower() + string[index + 1:len(string)]
    print(string)
