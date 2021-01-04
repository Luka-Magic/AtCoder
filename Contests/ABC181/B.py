n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for a,b in li:
    ans += int((a+b) * (b-a+1) * 0.5)
print(ans)