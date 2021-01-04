n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
c = 0
ans = 0
for a,b in li:
    if a==b:
        c+=1
        ans = max(c,ans)
    else:
        ans = max(c,ans)
        c=0
if ans >= 3:print('Yes')
else:print('No')