#Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
cinquentapares = []
num = 2
for i in range(0, 50):
    cinquentapares.append(num)
    num += 2
print(f"A soma dos 50 primeiros números pares é {sum(cinquentapares)}")
