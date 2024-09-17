A, B, C, D = map(int, input().split(" "))
if(B>C & D>A & C+D>A+B & C>=1 & D>=1 & A%2==0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
