r,y,g = input().split()
r = int(r)
y = int(y)
g = int(g)
n = int(input())
res = []
s = 0
for i in range(n):
    l = list(map(int,input().split()))
    res.append(l)
for i in range(n):
    if res[i][0]==0 or res[i][0] == 1:
        s+=res[i][1]
    if res[i][0] == 2:
        s+=res[i][1]
        s+=r
    if res[i][0] == 3:
        pass
print(s)

