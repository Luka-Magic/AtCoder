s1,s2,g1,g2 = map(int,input().split())
 
g2 = -g2
 
t = (g2-s2)/(g1-s1)
 
b = s2 - s1*t
 
print(-1 * b / t)