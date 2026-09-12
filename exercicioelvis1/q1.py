#1 - Uma palavra é palíndromo se, após converter todas as letras maiúsculas em minúsculas, é lida da mesma forma de trás para frente. 
#Com base em tal afirmação, escreva um programa que,dada uma string chamada palavra, informará se a palavra é palíndromo ou não.

palavra = input(str("insira uma palavra: "))
palin = palavra.lower()[::-1]

if palavra == palin:
    print(f"a palavra {palavra} é um palíndromo: {palin}")
else:
    print(f"a palavra {palavra} não é um palíndromo: {palin}")