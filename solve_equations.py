import math

a = float(input("Digite o valor de a: \n"))
b = float(input("Digite o valor de b: \n"))
c = float(input("Digite o valor de c: \n"))

delta = b**2 - 4*a*c

if delta >= 0:

  raiz_delta = math.sqrt(delta)
  x1 = (-b + raiz_delta) / (2*a)
  x2 = (-b - raiz_delta) / (2*a)

  print(f"As raízes da equação são x1 = {x1} e x2 = {x2}")
else:

  print("A equação não tem raízes reais")