Nome = input()
SalarioFixo = float(input())
ValorVendas = float(input())
Comissao = ValorVendas*0.15
SalarioFinal =SalarioFixo+Comissao
print(f"TOTAL = R$ {SalarioFinal:.2f}")