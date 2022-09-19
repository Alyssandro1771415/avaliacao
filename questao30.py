"""30. Fazer um programa em Python para determinar o quadrante ao qual pertence um
determinado ponto P(x, y)"""

pontoX = float(input("Coordenada X(-1 a 1):"))
pontoY = float(input("Coordenada Y(-1 a 1):"))

if pontoX == 0:
    print("As coordenadasse se encontram sobre o eixo das abscissas.")
elif pontoY == 0:
    print("As coordenas se encontram sobre o eixo das abcissas.")
elif pontoX == 0 and pontoY == 0:
    print("Os pontos informados estão no centro do ciclo trigonométrico.")
elif 0 < pontoX <= 1 and 0 < pontoY <= 1:
    print("1° Quadrante")
elif -1 <= pontoX < 0 and 0 < pontoY <= 1:
    print("2° Quadrante")
elif -1 <= pontoX < 0 and -1 <= pontoY < 0:
    print("3° Quadrante")
elif 0 < pontoX <= 1 and 0 > pontoY >= -1:
    print("4° Quadrante")
else:
    print("Coordenadas fora do raio do ciclo trigonométrico.")