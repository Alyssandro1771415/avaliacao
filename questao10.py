"""10. Tendo como dados de entrada a altura de uma pessoa, construa um programa Python
que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) – 58."""

altura = float(input("Altura: "))

pesoIdeal = (72.7*altura) - 58

print("Seu peso ideial é: "'{:.2f}'.format(pesoIdeal))
