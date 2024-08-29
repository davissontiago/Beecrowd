A , B, C = map(float, input().split())
Pi = 3.14159
AreaTri = (A*C)/2
AreaCirc = Pi*(C**2)
AreaTrap = ((A+B)*C)/2
AreaQuad = B**2
AreaRet = A*B
print(f"TRIANGULO: {AreaTri:.3f}")
print(f"CIRCULO: {AreaCirc:.3f}")
print(f"TRAPEZIO: {AreaTrap:.3f}")
print(f"QUADRADO: {AreaQuad:.3f}")
print(f"RETANGULO: {AreaRet:.3f}")