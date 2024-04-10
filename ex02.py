#Fazer um programa para encontrar todos os números pares entre 1 e 100
print("Os números pares entre 1 e 100 são:")
for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} ", end='')
