nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a seunda nota: "))
m = (nota1+nota2)/2
if m>= 7:
    print("você foi aprovado")
elif m >=4 and m<7:
    print("você ficou em recuperação.")
    rec = float(input("insira a nota da recuperação: "))
    print("a sua nota depois da recuperação é: ", (m+rec)/2)
else:
    print("você foi reprovado")