import random

r1 = random.randint(1, 50)
r2 = random.randint(1, 50)
r3 = random.randint(1, 50)
r4 = random.randint(1, 50)

lista1 = [r1, r2, r3, r4]
lista1min = min(lista1)
lista1max = max(lista1)

print(lista1)
print(f"o número mínimo dessa lista gerada aleatoriamente é {lista1min}")
print(f"o número máximo dessa lista gerada aleatoriamente é {lista1max}")