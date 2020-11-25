m,n = map(int,input().split())
res = []
for i in range(m):
    num = list(map(int,input().split()))
    res.append(num)
sums = 0
spa = []
each_spa = 0
for i in range(m):
    sums = sums + res[i][0]
for i in range(m):
    for j in range(1,n+1):
        each_spa += (-res[i][j])
    spa.append(each_spa)
    each_spa = 0
T = sums - sum(spa)
print("{} {} {}".format(T,spa.index(max(spa))+1,max(spa)))