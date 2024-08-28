Cod1, Num1, Valor1 = map(float, input().split(" "))
Cod2, Num2, Valor2 = map(float, input().split(" "))
Valor = (Num1*Valor1) + (Num2*Valor2)
print(f"VALOR A PAGAR: R$ {Valor:.2f}")