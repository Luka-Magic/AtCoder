r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())
 
d = c2 - c1
 
if r1==r2 and c1==c2:
    print(0)
    exit()
elif abs(c2-c1) == abs(r2-r1) or abs(c1-c2) + abs(r2-r1) <= 3:
    print(1)
    exit()
elif (r1+c1)%2 == (r2+c2)%2 or min(abs(r1-(r2-d)),abs(r1-(r2+d))) <= 3 or abs(c1-c2) + abs(r2-r1) <= 6:
    print(2)
    exit()
else:
    print(3)
    exit()