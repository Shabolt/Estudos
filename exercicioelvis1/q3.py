#3 - Escreva um programa que contenha uma função em Python para verificar se duas palavras são 
# anagramas (ou seja, se possuem exatamente as mesmas letras na mesma quantidade, independentemente 
# da ordem); o programa deve receber as duas strings, ignorar a diferença entre letras maiúsculas e 
# minúsculas, e retornar um valor 

def anagrama(ordem):
    palavra1 = input(f"insira a {ordem} palavra: ")
    p1low = palavra1.lower()
    anag = sorted(p1low)
    print(anag)
    return anag

def checagem():
    anagrama1 = anagrama("primeira")
    anagrama2 = anagrama("segunda")
    print(f"bool = {anagrama1 == anagrama2}")
    if anagrama1 == anagrama2:
        print("as duas palavras formam um anagrama.")
    else:
        print("as duas palavras não formam um anagrama.")

checagem()
