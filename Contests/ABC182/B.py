n = int(input())
li = list(map(int,input().split()))
 
ans = 0
ans_ = 0
for i in range(2,1001):
    temp = 0
    for j in li:
        if j % i == 0:
            temp += 1
    if temp >= ans_:
        ans_ = temp
        ans = i
 
print(ans)