def main():
    n,w = map(int,input().split())
    li = [list(map(int,input().split())) for _ in range(n)]
    li1 = [[a,c] for a,b,c in li]
    li2 = [[b,c] for a,b,c in li]
    
    li1.sort()
    li2.sort()
    # print(li1,li2)
    i = 0
    j = 0
    temp = 0
    for t in range(2*10**5+1):
        while i < n:
            if t != li1[i][0]:
                break
            temp += li1[i][1]
            i += 1
        while j < n:
            if t != li2[j][0]:
                break
            temp -= li2[j][1]
            j += 1
        # print(temp)
        if temp > w:
            print('No')
            exit()
    print('Yes')
if __name__ == '__main__':
    main()