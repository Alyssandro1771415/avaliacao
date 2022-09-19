"""3. Faça um Programa Python que peça a temperatura em graus Farenheit, transforme e
mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)."""

farenheit = float(input("Digite a temperatura em farenheit: "))

celsius = (5 * (farenheit-32) / 9)

print("{:.2f}°F equivale a {:.2f}°C".format(farenheit, celsius))