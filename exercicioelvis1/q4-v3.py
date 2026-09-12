#4 - Escreva um programa que tenha uma função que realize a 
# contagem de itens numa tupla. Além da contagem de itens, 
# realize a separação dos valores ímpares e pares em duas 
# tuplas diferentes. Para gerar a tupla inicial utilize o 
# construtor tuple(range(0,101)) 

tuplaex = tuple(range(0, 101))
tuplapar = []
tuplaimp = []

def tuplacontador():
    tuplacont = 0
    for i in tuplaex:
        tuplacont += 1
    print(tuplacont)
        
def tuplaimp_par():
    for i in tuplaex:
        if i % 2 == 0:
            tuplapar.append(i)
        else:
            tuplaimp.append(i)
    print(f"os números pares da tupla são: {tuplapar}.")
    print(f"os números ímpares da tupla são: {tuplaimp}.")

#-----------------
tuplacontador()
tuplaimp_par()