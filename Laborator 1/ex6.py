def palindrome(number):
    aux = number
    reversed = 0
    while aux > 0:
        c = int(aux % 10)
        reversed = reversed * 10 + c
        aux = int(aux // 10)
    if (number == reversed):
        print("Numarul este palindrom")
    else:
        print("Numarul nu este palindrom")

if __name__ == "__main__":
    nr = input("Scrie numarul\n")
    palindrome((int)(nr))
