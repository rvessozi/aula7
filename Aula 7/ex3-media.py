print("Notas escolares")
print("Informe sua nota de 0 a 10")
nota1 = -1
while(nota1<0 or nota1 > 10):
    nota1 = float(input("Digite sua nota: "))
    if (nota1<0 or nota1>10):
       print("Nota invalida")

nota2 = -1
while(nota2<0 or nota2 >10):
    nota2 = float(input("Digite sua nota: "))
    if (nota2<0 or nota2 >10):
        print("Nota invalida")

nota3 = -1
while(nota3<0 or nota3 >10):
    nota3 = float( input("Digite sua nota: "))
    if(nota3<0 or nota3>10):
        print("Nota invalida")

media = (nota1+nota2+nota3)/3

if (media>=7):
    print("Aprovado")
else: 
    print("Reprovado")