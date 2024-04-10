#Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.
num = int(input("Digite um número inteiro (entre 1 e 10): "))
while 1 > num  or num > 10:
    print("O cálculo só pode ser feito com valores entre 1 e 10!")
    num = int(input("Tente novamente: "))
print(f"A tabuada de {num} é:")
print("="* 15)
for i in range(1, 11):
    print(f" {num} x {i} = {num*i}")
print("="* 15)

