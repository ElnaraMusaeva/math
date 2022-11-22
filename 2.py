import math
n = int(input())
a, b, c, med = int, int, int, int
def median(a, b, c):
    return math.sqrt((2*b**2 + 2*a**2 - c**2)/4)
def F(n):
    q = 0
    for c in range(1, n+1):
        for b in range(1, c+1):
            for a in range(1, b+1):
                if a + b > c and c + b > a and  c + a > b:
                    if median(a, b, c) - int(median(a, b, c)) == 0.0:
                        q+=1
    print(f"F({n}) = {q}")                    
F(n)
