n = int(input())
ans = 0
 
def change(N,shinsu):
    keta=0
    for i in range(10**9):
        if N<shinsu**i:
             keta+=i
             break
    ans=[0]*keta
    check=0
    for i in range(1,keta+1):
        j=N//(shinsu**(keta-i))
        ans[check]=j
        check+=1
        N-=(j)*(shinsu**(keta-i))
    return ans
 
for i in range(1,n+1):
    if '7' in list(str(i)):continue
    if 7 in change(i, 8):continue
    ans += 1
print(ans)