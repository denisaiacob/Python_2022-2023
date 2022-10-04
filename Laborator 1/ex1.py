def cmmdc(a, b):
    if b == 0:
        return a
    else:
        return cmmdc(b, a % b)


nr = input("Pentru cate numere doresti sa aflii CMMDC?\n")
nr = (int)(nr)
a = input("Scrie primul numar\n")
b = input("Scrie al doilea numar:\n")
a = (int)(a)
b = (int)(b)
a = cmmdc(a, b)
for index in range(3, nr + 1):
    b = input("Scrie urmatorul numar\n")
    b = (int)(b)
    a = cmmdc(a, b)
print("Cel mai mare divizor comun este: %d" % (a));
