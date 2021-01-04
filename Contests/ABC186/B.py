h,w = map(int,input().split())
li = [[*map(int,input().split())] for _ in range(h)]
 
import numpy as np
 
li = np.array(li)
s = np.min(li)
li_new = li - s
print(np.sum(li_new))