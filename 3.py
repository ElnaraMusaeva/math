import combinations
def triang(a, b, c):
    if round(a**2, 5) == round(b**2+c**2-2*b*c*cos(pi/4), 5) or round(b**2, 5) == round(a**2 +c**2-2*b*c*cos(pi/4), 5) or round(c**2, 5) == round(a**2+b**2-2*a*b*cos(pi/4), 5):
        return True
    else: 
        return False
triangles = []
g = int(input())
e = int(input())
arr1 = list(range(1, g+1))
arr2 = list(range(-e, g+1))
h = comb(len(arr2), 3)
val = []
cnt = 0
l1 = itertool.combinations(arr2, 3)
l2 = list(l1)
for i in arr1:
    for j in l2:       
        j = list(j)
        j.sort()
        k = [j[0], j[0]**2/i]
        l = [j[1], j[1]**2/i]
        m = [j[2], j[2]**2/i]
        v = [k, l, m]
        if v not in val:
            a = dist(v[0], v[1])
            b = dist(v[0], v[2])
            c = dist(v[2], v[1])
            if triang(a, b, c):                
                cnt += 1
            val.append([k, l, m])
print(cnt)
