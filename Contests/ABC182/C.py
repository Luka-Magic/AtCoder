n = list(map(int,list(input())))
 
from collections import Counter
C = Counter(n)
a1 = C[1]+C[4]+C[7]
a2 = C[2]+C[5]+C[8]
a0 = C[3]+C[6]+C[9]
 
if a0==0 and 1<=a1<=2 and a2==0:
    print(-1)
    exit()
if a0==0 and 1<=a2<=2 and a1==0:
    print(-1)
    exit()
 
# if abs(a1-a2)%3 == 0:#どんなときも成り立つ
#     print(0)
#     exit()
 
if a1%3==0 and a2%3==1:
    print(1)
    exit()
 
if a2%3==0 and a1%3==1:
    print(1)
    exit()
 
print(abs(a1-a2)%3)