n = int(input())
nums = []
for i in range(n):
    nums.append(input())
# print(nums)
for i in range(n):
    nums[i] = nums[i].replace('x', '*')
    nums[i] = nums[i].replace('/','//')
# print(nums)
res = []
for i in range(n):
    if eval(nums[i]) == 24:
        res.append('Yes')
    else:
        res.append('No')
for i in range(n):
    print(res[i])

