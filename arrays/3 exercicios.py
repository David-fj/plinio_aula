# EXERCICIO 1
'''
aprovados = 0

for i in range(10):
    notas = []
    for c in range(4):
        notas.append(float(input(f"Digite a {c+1}º nota do {i+1}º aluno: ")))
    if sum(notas)/4 >= 7:
        aprovados += 1
print(f"Alunos aprovados: {aprovados}")
'''
# EXERCICIO 2
'''
altura = []
idade = []

for i in range(5):
    altura.append(float(input(f"Digite a altura da {i+1}º pessoa: ")))
    idade.append(int(input(f"Digite a idade da {i+1}º pessoa: ")))

altura.reverse()
idade.reverse()

print(f"Alturas: {altura}\nIdades: {idade}")
'''
# EXERCICIO 3
'''
l = []
for i in range(10):
    l.append(int(input(f"Digite o {i+1}º número: "))**2)
print(f"Soma: {sum(l)}")
'''
