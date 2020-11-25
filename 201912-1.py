
n = int(input())
res = []
for i in range(4):
    res.append(0)
i=1
while n:
    s = str(i)
    if i % 7==0 or '7' in s:
        res[i%4-1]+=1
        i=i+1
    else:
        n-=1
        i+=1


for i in range(4):
    print(res[i])