def fatorial():
    numInit = int(input("numrange = "))
    for i in range (numInit, 1, -1):
        numInit *= (i-1)
    print(numInit)

fatorial()