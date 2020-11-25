n = int(input())
nums = list(map(int,input().split()))
res = []
res.append(int((nums[0]+nums[1])/2))
for i in range(1,n-1):
    res.append(int((nums[i-1]+nums[i]+nums[i+1])/3))
res.append(int((nums[-1]+nums[-2])/2))
for i in range(n):
    print(res[i],end=' ')


