n = int(input())
count=0
nums = list(map(int,input().split()))
for i in range(1,n-1):
    if (nums[i]>nums[i-1] and nums[i]>nums[i+1]) or (nums[i]<nums[i-1] and nums[i]<nums[i+1]):
        count+=1
print(count)

