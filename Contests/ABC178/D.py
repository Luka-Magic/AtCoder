mod = 10**9+7
 
from operator import mul
from functools import reduce
 
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under
 
s = int(input())
if s==1 or s==2:
    print(0)
    exit()

pk_num = s//3-1
ans = 1
for i in range(pk_num):
    pk = (i+2)*3
    g = s - pk
    b = i+2
    ans += cmb(g+b-1,b-1)
    ans %=  mod
print(ans)
mod = 10**9+7