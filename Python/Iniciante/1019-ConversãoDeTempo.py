Tempo = int(input())
Horas = Tempo//60//60
Minutos = Tempo//60%60
Segundos = Tempo%60
print(f"{Horas}:{Minutos}:{Segundos}")