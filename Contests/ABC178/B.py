a,b,c,d = map(int,input().split())
 
ans = -float('inf')
 
ans = max(a*c,ans)
ans = max(a*d,ans)
ans = max(b*c,ans)
ans = max(b*d,ans)
 
print(ans)