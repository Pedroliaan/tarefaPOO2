num1 = int(input("insira o primeiro numero: "))
num2 = int(input("insira o segundo numero: "))
num3 = int(input("insira o terceiro numero: "))

if num1< num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print("esses valores podem ser o lado de um triangulo")
else:
        print("esses valores não podem ser o lado de um triangulo")