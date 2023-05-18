p1 = float(input("insira o primeiro preço: "))
p2 = float(input("insira o segundo preço: "))
p3 = float(input("insira o terceiro preço: "))

if p1<p2 and p2<p3 and p1<p3:
    print("compre o produto 1")
elif p1>p2 and p2<p3:
    print("compre o produto 2")
else:
    print("compre o produto 3")