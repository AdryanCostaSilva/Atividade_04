#Leia várias idades e calcule a média entre as idades (usar uma variável para idade).
idade = 0
todasidades = []
while True:
    idade = int(input("Digite a idade (apenas valores maior que 0):"))
    resp = ' '
    if idade < 0:
        continue
    else:
        todasidades.append(idade)
    while resp not in 'SsNn':
        resp = str(input("Quer adicionar mais uma idade (S/N): "))
    if resp in 'Nn':
        break
print(f"A média das idades {todasidades} é {sum(todasidades)/len(todasidades)}.")