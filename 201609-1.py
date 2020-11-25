n = int(input())
m = 0
nums = list(map(int,input().split()))
for i in range(1,n):
    if abs(nums[i]-nums[i-1])>m:
        m = abs(nums[i]-nums[i-1])
print(m)

