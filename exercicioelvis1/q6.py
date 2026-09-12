#6 - Escreva um programa que tenha a função removeImpar(), essa função deve receber como parâmetro uma 
# lista composta por números e deve remover os números ímpares presentes na lista. Para gerar a lista 
# inicial utilize o construtor  list(range(0,101)) .

lista1 = list(range(0, 101))

def removeImpar():
    for i in lista1:
        if i % 2 == 1:
            lista1.remove(i)
    print(lista1)

removeImpar()