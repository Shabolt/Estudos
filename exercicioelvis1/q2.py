#2 - Considere que você está desenvolvendo um sistema de secretaria acadêmica em Python que gerencia o cadastro de um estudante utilizando 
#um dicionário com as chaves 'nome', 'matricula', 'nascimento', 'curso' e 'disciplinas' (sendo esta última uma lista); o programa deve 
#interagir com o usuário para permitir a inserção de novas disciplinas nessa lista interna do dicionário e, ao final, exibir todas as 
#informações atualizadas do aluno na tela; Diante dessas informações, escreva um programa que realize o comportamento descrito.

dict1 = {
    "nome":"Allan",
    "matricula":"03361568",
    "nascimento":"15/06/2003",
    "curso":"ADS - Análise e Desenvolvimento de Sistemas",
    "disciplinas":[]
}

disc1 = str(input("insira a primeira disciplina: "))
disc2 = str(input("insira a segunda disciplina: "))
disc3 = str(input("insira a terceira disciplina: "))

dict1["disciplinas"].append(disc1)
dict1["disciplinas"].append(disc2)
dict1["disciplinas"].append(disc3)

print(dict1)