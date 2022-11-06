def process_item(x):
    x=x+1
    while 1:
        d=0
        for i in range(2,int(x/2+1)):
            if x%i==0:
                d=d+1
        if d!=0:
            x=x+1
        else:
            return x
x=int(input("Dati x "))
