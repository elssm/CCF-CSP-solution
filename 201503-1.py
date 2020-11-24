m,n = map(int,input().split())
res=[]
for i in range(m):
    num = list(map(int,input().split()))
    res.append(num)
for i in range(n):
    for j in range(m):
        print(res[j][n-i-1],end=' ')
    print()
