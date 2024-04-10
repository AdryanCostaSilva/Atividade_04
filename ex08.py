#Faça um algoritmo que leia um número positivo e imprima seus divisores.
num = 0
while num <= 0:
    num = int(input("Digite um número inteiro positivo: "))
divisivel = []
for i in range(1,num+1):
    if num % i == 0:
        divisivel.append(i)
if len(divisivel) > 2:
    print(f"O número {num} é divísivel pelos números {divisivel}.")
else:
    print(f"O número {num} é divísivel pelos números {divisivel}, ou seja, é primo.")
