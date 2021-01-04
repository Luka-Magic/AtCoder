n = int(input())
 
li = [input() for _ in range(n)]
import re
 
li.sort()
li_ = [s[1:] for s in li if re.search('^!', s)]
li = set(li)
li_ = set(li_)
ans = li & li_
 
if not ans:
    print('satisfiable')
else:print(list(ans)[0])