def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        exit()
    
    li = [0] + list(map(int,input().split())) + [n+1]
    li.sort()
    
    interval = [li[i+1]-li[i]-1 for i in range(len(li)-1) if li[i+1]-li[i]-1>0]
 
    if len(li) == n+2:
        print(0)
        exit()
    
    import math
    
    k = min(interval)
    ans = 0
    for i in interval:
        ans += math.ceil(i/k)
    
    print(ans)
if __name__ == '__main__':
    main()