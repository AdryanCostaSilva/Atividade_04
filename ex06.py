#Utilizando a estrutura de repetição for, faça um programa que receba 10 números e conte quantos deles estão no intervalo [10,20] e 
#quantos deles estão fora do intervalo.
fora = []
dentro = []
for i in range(0, 10):
    num = float(input("Digite um número: "))
    if num >= 10 and num <= 20:
        dentro.append(num)
    else:
        fora.append(num)
print(f"Foram digitados {len(fora)} fora do intervalo [10, 20], são eles {fora}.")
print(f"Foram digitados {len(dentro)} dentro do intervalo [10, 20], são eles {dentro}.")
