n,m,t = map(int,input().split())
ans = n
li_temp = [[*map(int,input().split())] for _ in range(m)]
li_temp.append([t,0])
li = [[0,li_temp[0][0]]]
for i in range(m):
    li.append(li_temp[i])
    li.append([li_temp[i][1],li_temp[i+1][0]])
 
for i in range(m):
    i *= 2
    ans -= li[i][1]-li[i][0]
    if ans <= 0:
        print('No')
        exit()
    ans += li[i+1][1]-li[i+1][0]
    ans = min(n,ans)
    
ans -= li[-1][1]-li[-1][0]
if ans <=0:
    print('No')
else:print('Yes')