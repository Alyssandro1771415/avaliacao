"""24. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

a.          Até 5 Kg         Acima de 5 Kg
ii. Morango R$ 2,50 por Kg R$ 2,20 por Kg
iii. Maçã R$ 1,80 por Kg R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um programa Python para ler a
quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o
valor a ser pago pelo cliente."""

morango = float(input("Quantidade de morangos em Kg: "))
precoMorango = 2.50
maca = float(input("Quantidade de maçãs em Kg: "))
precoMaca = 1.80

if morango > 5:
    precoMorango = 2.20

if maca > 5:
    precoMaca = 1.50

valorCompra = morango*precoMorango+maca*precoMaca

if morango+maca >= 8 or valorCompra >= 25:
    valorCompra = valorCompra * 0.9

print(f"Valor a pagar: R${valorCompra:.2f}")
