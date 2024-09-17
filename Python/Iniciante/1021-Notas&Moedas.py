entrada = float(input())
valor = int(round(entrada * 100))

notas = [10000, 5000, 2000, 1000, 500, 200] 
print("NOTAS:")
for nota in notas:
    quant = valor // nota
    print(f"{quant} nota(s) de R$ {nota / 100:.2f}")
    valor = valor % nota

moedas = [100, 50, 25, 10, 5, 1]
print("MOEDAS:")
for moeda in moedas:
    quant = valor // moeda
    print(f"{quant} moeda(s) de R$ {moeda / 100:.2f}")
    valor = valor % moeda

