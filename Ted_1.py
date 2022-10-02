nota1 = float(input("Primeira Nota: "))
nota2 = float(input("Primeira Nota: "))
nota3 = float(input("Primeira Nota: "))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print(f"Sua média foi {media:.1f}\nAprovado com destinção!!")
elif media < 10 and media >= 7:
    print(f"Sua média foi {media:.1f}\nAprovado!!")
else:
    print(f"Sua média foi {media:.1f}\nReprovado!!")