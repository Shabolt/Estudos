#8 - Escreva um programa que tenha uma função chamada verificaTupla, essa função deve receber uma tupla que 
# consiste em nomes de frutas. A tupla será composta por : ‘maca’ , ‘banana’, ‘abacaxi’, ‘limão’, ‘laranja’, 
# ‘goiaba’. eu programa deve verificar se existe a presença das frutas : limão, maçã e kiwi, caso a fruta 
# esteja na tupla, seu programa deve imprimir uma mensagem informando que a fruta está presente na tupla, 
# se não estiver presente, seu programa deve informar que a fruta não está presente na tupla.

def checarfruta():
    frutauser = input("insira a fruta a ser verificada: ")
    return frutauser

tuplafrutas = ('maçã', 'banana', 'abacaxi', 'limão', 'laranja', 'goiaba')

print(tuplafrutas)

fruta = checarfruta()

if fruta in tuplafrutas:
    print(f"a fruta {fruta} está na tupla")
else:
    print(f"a fruta {fruta} não se encontra na tupla")