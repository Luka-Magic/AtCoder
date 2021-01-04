from collections import Counter
 
s = input()
 
if len(s) == 1:
    if s=='8':
        print('Yes')
    else:
        print('No')
    exit()
        
if len(s) == 2:
    if int(s)%8 == 0 or int(s[::-1])%8 == 0:
        print('Yes')
    else:
        print('No')
    exit()
 
c = Counter(s)
 
#print(c)
for i in range(104,1000,8):
    c2 = Counter(str(i))
    for k,v in c2.most_common():
        if c[k] < v:
            break
    else:
        print('Yes')
        break
else:
    print('No')