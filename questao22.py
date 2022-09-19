"""22. Faça um Programa Python que peça um número correspondente a um determinado
ano e em seguida informe se este ano é ou não bissexto."""


ano = int(input("Ano: "))

if ano % 4 == 0 and ano % 100 == 1:
    print("Ano bissexto.")
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print("Anobissexto:")
else:
    print("Ano não bissexto.")