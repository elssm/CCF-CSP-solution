n,k = map(int,input().split())
nums = list(map(int,input().split()))
s = 0
count = 0
for i in range(n):
    s+=nums[i]
    if s>= k or i==n-1:
        count+=1
        s = 0
        continue
print(count)



