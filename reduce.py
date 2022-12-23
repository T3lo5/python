from functools import reduce

def soma(x, y):
    return x + y

lista = [1, 4, 5, 6, 7, 5, 423, 65, 65, 4, 3]

soma = reduce(soma, lista)

print("A lista original é: \n")
print(lista)

print("Sua soma é: \n")
print(soma)