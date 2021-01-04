N = int(input())
li = list(map(int,input().split()))
humi = li[0]
ans = 0
for l in li[1:]:
    if l <= humi:
        ans += humi - l
    else:
        humi = l
print(ans)