def dano(n,a,b,c):
    if n == 1:
      print(a,"--->",c)
      return None
      dano(n-1,a,c,b)
      print(a,"--->",c)
      dano(n-1,b,a,c)

n, a, b, c = 3,"A","B","C"      

dano(3,A,B,C)
time
