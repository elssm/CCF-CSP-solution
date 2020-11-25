n = int(input())
nums = list(map(int,input().split()))
nums = sorted(nums)
cha = nums[1]-nums[0]
for i in range(2,n):
    if nums[i] - nums[i-1] < cha:
        cha = nums[i] - nums[i-1]
print(cha)


