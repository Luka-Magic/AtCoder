x,k,d = map(int,input().split())
x_max = x+k*d
x_min = x-k*d
if x_max<=0:print(-x_max)
elif x_min>=0:print(x_min)
else:
    t = x_max%(2*d)
    t2 = -t+2*d
    print(min(t,t2))