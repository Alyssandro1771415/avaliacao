"""7. Escreva um programa Python que leia três números inteiros e positivos (A, B, C) e
calcule a seguinte expressão:"""

valorA = int(input("Digite um valor:"))
valorB = int(input("Digite um valor:"))
valorC = int(input("Digite um valor:"))

if valorA < 0 or valorB < 0 or valorC<0:
    print("Valores digitados inválidos, reinicie o programa e insira valores válidos.")
    exit()

R = (valorA+valorB)**2
S = (valorB+valorC)**2

valorD = (R+S)/2

print("O resultado da equação é {:.2f}.".format(valorD))