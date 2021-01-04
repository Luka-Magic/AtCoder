n = int(input())
 
li = [list(map(int,input().split())) for _ in range(n)]
 
from itertools import combinations
 
for a,b,c in list(combinations(li,3)):
    x1 = a[0]-b[0]
    y1 = a[1]-b[1]
    x2 = a[0]-c[0]
    y2 = a[1]-c[1]
    if x1*y2-y1*x2 == 0:
        print('Yes')
        exit()
print('No')