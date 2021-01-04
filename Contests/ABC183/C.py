n,k = map(int,input().split())
 
li = [list(map(int,input().split())) for _ in range(n)]
 
from itertools import permutations
 
ans = 0
 
for i in list(permutations(range(2,n+1),n-1)):
    temp_li =[1] + list(i) + [1]
    temp = 0
    for j in range(n):
        temp += li[temp_li[j]-1][temp_li[j+1]-1]
    if temp == k:
        ans += 1
print(ans)