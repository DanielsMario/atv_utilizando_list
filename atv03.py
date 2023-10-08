num1 = []
for i in range(10):
    num2 = float(input(f"Digite o {i + 1}º número: "))
    num1.append(num2)
par = []
impar = []
positivo = []
negativo = []
zero = []
for num2 in num1:
    if num2 % 2 == 0:
        par.append(num2)
    else:
        impar.append(num2)

    if num2 > 0:
        positivo.append(num2)
    elif num2 < 0:
        negativo.append(num2)
    else:
        zero.append(num2)
print("Números ímpares:", impar)
print("Números pares:", par)
print("Números positivos:", positivo)
print("Números negativos:", negativo)
print("Zeros:", zero)
