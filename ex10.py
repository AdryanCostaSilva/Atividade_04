#Dada a lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6] imprima o número que se repete mais vezes.
lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
maior = []
for i in lista:
    maior.append(lista.count(i))
maisrepetido = lista[maior.index(max(maior))]
print(f"O número mais repetido na lista foi o {maisrepetido}.")
