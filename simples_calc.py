num1 = float(input("Qual o primeiro numero?: \n"))
sinal = input("Digite o sinal da operação (+, -, * ou /): \n")
num2 = int(input("Qual o segundo número?: \n"))

if sinal == "+":
  resultado = num1 + num2
elif sinal == "-":
  resultado = num1 - num2
elif sinal == "*":
  resultado = num1 * num2
elif sinal == "/":
  resultado = num1 / num2
else:
  print("Sinal inválido")

print(f"Resultado: {resultado}")