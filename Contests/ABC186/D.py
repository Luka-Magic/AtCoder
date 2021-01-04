n = int(input())
li = list(map(int,input().split()))
 
if n == 2:
    print(abs(li[0]-li[1]))
    exit()
 
li.sort()
ans = 0
li_diff = [li[i+1] - li[i] for i in range(n-1)]
if (n-1)%2 == 0:
    li1 = li_diff[:(n//2)]
    li2 = li_diff[(n//2):][::-1]
    s = 0
    for i in range((n-1)//2):
        s += n-(2*i+1)
 
        ans += s * (li1[i] + li2[i])
 
else:
    li1 = li_diff[:((n//2)-1)]
    li2 = li_diff[(n//2):][::-1]
    p = li_diff[n//2-1]
    s = 0
    for i in range((n-1)//2):
        s += n-(2*i+1)
        ans += s * (li1[i] + li2[i])
    ans += p * (s + 1)
print(ans)