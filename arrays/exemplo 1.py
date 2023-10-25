# Criar uma lista definida pelo usuario - quantidade de elementos e os elementos

qtd = int(input("Informe a quantidade de elementos: "))

lista = []

for i in range(qtd):
    valores = int(input("Informe o valor: "))
    lista.append(valores)
lista.sort()
print(lista)
