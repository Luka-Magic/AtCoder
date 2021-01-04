from itertools import combinations
 
[N],*li = [list(map(int,i.split())) for i in open(0)]
li = li[0]
count = 0
for k in combinations(li,3):
    k = sorted(list(k))
    if k[2]<k[0]+k[1] and k[0]!=k[1] and k[1]!= k[2]:
        count += 1
print(count)