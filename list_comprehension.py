x = [1, 3, 4, 5, 6, 9]
y = [i**2 for i in x]
z = [i for i in x if i%2==1]

print(x)
print("A lista ao quadrado é: \n")
print(y)
print("A lista com os números ímpares é: \n")
print(z)
