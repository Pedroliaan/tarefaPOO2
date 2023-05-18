p1 = float(input("insira a primeira altura: "))
p2 = float(input("insira a segunda altura: "))
p3 = float(input("insira a terceira altura: "))

maior = p1

if p1==p2 or p2==p3 or p1==p3:
    print("Há, pelo menos, 2 pessoas com a mesma estatura")
elif (p2 > maior):
        maior = p2
        print("o maior é: ", maior)
elif (p3 > maior):
        maior = p3
        print("o maior é: ", maior)

    