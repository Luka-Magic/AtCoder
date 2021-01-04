n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
ans = 0
from itertools import combinations
for a,b in combinations(li,2):
    x,y = a[0],a[1]
    z,w = b[0],b[1]
    if z-x == 0:
        continue
    d = (w-y)/(z-x)
    if -1 <= d <= 1:
        ans += 1
print(ans)