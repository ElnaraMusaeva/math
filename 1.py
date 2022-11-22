import math
def p(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0:
            q+=1
    if q == 1:
        return 1
    return 0
def quad(n):
    s = int(math.sqrt(n))
    if s*s==n:
        return s
    return -1
def S(n):
    q = 0
    for i in range(1, int(math.sqrt(n))+1):
        if quad(n-i**2)>=i:
            q+=i
    return q
  q = 0
for i in range(1, 37):
    n = i*4+1
    if p(n)==True:
        q+=S(n)
print(q)
