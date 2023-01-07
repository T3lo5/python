import numpy as np

# Crie uma matriz de 10 zeros

print(np.zeros(10), "\n")

# Crie uma matriz de 10 uns

print(np.ones(10), "\n")

# Crie uma matriz de 10 cincos

print((np.ones(10)*5), "\n")

# Crie um array de inteiros de 10 a 50 

print(np.arange(10,51), "\n")

# Crie um array de todos os números pares de 10 a 50

print(np.arange(10,51, 2), "\n")

# Crie uma matriz 3x3 com valores variando de 0 a 8

print(np.arange(9).reshape(3,3), "\n")

# Crie uma matriz identidade 3x3

print(np.eye(3), "\n")

# Use NumPy para gerar numeros aleatórios entre 0 e 1 

print(np.random.rand(1), "\n")

# Use NumPy para gerar um array de 25 números amostrados de uma distribuição normal padrão

print(np.random.randn(25), "\n")    

# Crie uma matriz 10x10 com valores variando de 0,01 a 1

print((np.arange(1,101).reshape(10,10) / 100), "\n")

# Crie um array de tamanho 20 igualmente espaçado entre 0 e 1 

print(np.linspace(0,1,20), "\n")

# Indexaçao e seleçao 

mat = np.arange(1,26).reshape(5,5)

print(mat[2:,1:], "\n")

print(mat[3,4], "\n")

print(mat[:3,1:2], "\n")

print(mat[4,:], "\n")

print(mat[3:5,:], "\n")

# Obter a soma de todos os valores no "mat"

print("a soma do mat é:", mat.sum(), "\n")

# Obter o desvio padrao dos valores em mat

print("O desvio padrao em mat: ", mat.std(), "\n")

# Obter a soma de todas as colunas em mat

print("A soma de todas as colunas de mat: ", mat.sum(axis=0), "\n")


