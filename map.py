def dobro(x):
    return x * 2

valor = [1, 5, 6, 7, 9, 43]

valor_dobrado = map(dobro, valor)

valor_dobrado = list(valor_dobrado)
print("A lista original é: \n")
print(valor)
print("A lista dobrada é: \n")
print(valor_dobrado)

