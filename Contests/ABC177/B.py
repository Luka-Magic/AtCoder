S = list(input())
T = list(input())
 
s = len(S)
t = len(T)
 
ans = float('inf')
 
for i in range(s-t+1):
    k = 0
    for j in range(t):
        if S[i+j] != T[j]:
            k += 1
    ans = min(k,ans)