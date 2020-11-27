#不知道为什么只有80的正确率
nums = input().split('-')
sum = int(nums[0])
j=2
for i in range(3):
    sum += int(nums[1][i])*j
    j+=1
for i in range(5):
    sum+= int(nums[2][i])*j
    j+=1
if str(sum % 11) == nums[3]:
    print('Right')
elif str(sum%11) != nums[3] and sum%11!=10:
    nums[3] = str(sum%11)
    s = ''
    for i in range(len(nums) - 1):
        s += nums[i]
        s += '-'
    s += nums[3]
    print(s)
else:
    nums[3] = 'X'
    s = ''
    for i in range(len(nums)-1):
        s+=nums[i]
        s+='-'
    s+=nums[3]
    print(s)

