#Ler 10 números e imprimir quantos são pares e quantos são ímpares.
impares = []
pares = []
for i in range(1, 11):
    num = int(input(f"Digite o {i}° número inteiro: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"Foram digitados {len(pares)} pares, foram eles {pares}.")
print(f"Foram digitados {len(impares)} impares, foram eles {impares}.")
