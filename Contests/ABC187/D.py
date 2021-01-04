n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
su_li = [a+b for a,b in li]
d_li = [a+b[0] for a,b in zip(su_li, li)]
 
d_li.sort(reverse=True)
 
su = 0
for i in li:
    su += i[0]
ans = 0
 
for i in d_li:
    ans += 1
    su -= i
    if su < 0:
        print(ans)
        break