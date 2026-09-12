#7 - Escreva um programa que realize o cálculo do fatorial de um número, a partir do valor inserido pelo 
# usuário. Podem ser utilizados na resolução: funções recursivas, funções lambdas ou funções puras.

#método 1 - import math

#import math

#numuser = 0

#def inputuser():
#    while True:
#        try:
#            numuser = int(input("insira o número a ser calculado: "))
#            return numuser
#        except ValueError:
#            print("insira um número válido")
       

#numfat = inputuser()

#numfatorado = math.factorial(numfat)
#print(numfatorado)

#método 2 - manual

def fatorial():
    numInit = int(input("numrange = "))
    for i in range (numInit, 1, -1):
        numInit *= (i-1)
    print(numInit)

fatorial()

#esse foi pancada seca, pensei umas 12x em passar pelo gemini, mas dei cabo na mão mesmo