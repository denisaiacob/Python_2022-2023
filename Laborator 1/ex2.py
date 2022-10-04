if __name__ == "__main__":
    string = input("Scrie fraza\n")
    vowels = "AaEeIiOoUu"
    nr = 0
    for index in range(0, len(string)):
        if string[index] in vowels:
            nr = nr + 1
    print("Numarul de vocale este: %d " % (nr))
