n = int(input())
 
if n==1:
    print(0)
    exit()
 
ans = 1
ans += (n-2)*2
 
for i in range(2,n-1):
    ans += (n-1)//i-1
print(ans)