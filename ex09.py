#Faça um algoritmo que leia 10 números inteiros, armazene-os em uma lista e imprima em ordem crescente.
lista = []
for i in range(0, 10):
    num =int(input(f"Digite o {i + 1}° número inteiro:"))
    if num < 0:
        continue
    lista.append(num)
print(f"Lista: {lista}")
lista.sort()
print(f"Lista ordenada de forma crescente: {lista}")
