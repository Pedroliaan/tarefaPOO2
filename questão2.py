num1 = int(input("insira o primeiro numero: "))
num2 = int(input("insira o segundo numero: "))
num3 = int(input("insira o terceiro numero: "))

if num1<num2<num3:
    print(num1, num2, num3)
elif num1>num2<num3:
    print(num2, num1, num3)
elif num1>num2>num3:
    print(num3, num2, num1)
elif num1<num3<num2:
    print(num1, num3, num2)
elif num1<num3>num2:
    print(num2, num3, num1)