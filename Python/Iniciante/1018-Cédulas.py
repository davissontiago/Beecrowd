Valor = int(input())
print(Valor)
Notas = [100,50,20,10,5,2,1]
for Nota in Notas:
    quant = Valor // Nota
    print(f"{quant} nota(s) de R$ {Nota},00")
    Valor = Valor%Nota