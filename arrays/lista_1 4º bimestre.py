# EXERCICIO 1
'''
lista = [1, 5, 10]
print(f"Lista: {lista}")
print("Elementos: ")
for i in lista:
    print(i)
'''
# EXERCICIO 2
'''
lista = []
for i in range(int(input("Informe o número de limite: "))):
    lista.append(i+1)
print(lista)
'''
# EXERCICIO 3
'''
lista = []
for i in range(int(input("Informe o número de limite: ")), 0, -1):
    lista.append(i)
print(lista)
'''
# EXERCICIO 4
'''
lista = []
for i in range(int(input("Inicio: ")), int(input("Fim: "))+1):
    lista.append(i)
print(lista)
'''
# EXERCICIO 5
'''
lista = []
start = int(input("Inicio: "))
end = int(input("Fim: "))
for i in range(end, start-1, -1):
    lista.append(i)
print(lista)
'''
# EXERCICIO 6
'''
l = []
qtd = int(input("Informe a quantidade de elementos: "))
for i in range(qtd):
    l.append(int(input(f"Informe o número de índice {i} da lista: "))*2)
print(l)
'''
# EXERCICIO 7
'''
l = []
n = int(input("Informe um número para a tabuada: "))
for i in range(1, 11):
    l.append(n*i)
print(f"Tabuada do {n}: {l}")
'''
# EXERCICIO 8
'''
n = []
qtd = int(input("Informe a quantidade de notas: "))
for i in range(qtd):
    n.append(int(input(f"Informe a {i+1}º nota: ")))
print(f"Notas: {n}\nMédia: {sum(n)/qtd:.1f}")
'''
# EXERCICIO 9
'''
n = []
par = []
impar = []
for i in range(int(input("Informe a quantidade de números a serem digitados: "))):
    valor = int(input(f"Informe o {i+1}º número: "))
    n.append(valor)
    if valor%2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f"Números informados: {n}\nNúmeros Pares: {par}\nNúmeros Ímpares: {impar}")
'''
# EXERCICIO 10
'''
n = []
s = 0
m = 1
qtd = int(input("Informe a quantidade de elementos: "))
for i in range(qtd):
    valor = int(input(f"Informe o {i+1}º número: "))
    n.append(valor)
    s += valor
    m = m*valor
print(f"A lista é: {n}\nA soma é: {s}\nA multiplicação: {m}")
'''
# EXERCICIO 11

l = []
s = 0
nome = input("Informe o nome do(a) atleta: ")
for i in range(5):
    valor = float(input(f"Informe o {i+1}º salto: "))
    l.append(valor)
    s+= valor
print(f"Atleta: {nome}\nSaltos: {l}\nA média dos saltos: {s/5:.2f}m")