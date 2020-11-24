n=int(input())
nums = list(map(int,input().split()))
mid = int(n/2)
c1=0
c2=0
snums = sorted(nums)
for i in range(n):
    if nums[i]>snums[mid]:
        c1+=1
    elif nums[i]<snums[mid]:
        c2+=1
if c1==c2:
    print(snums[mid])
else:
    print('-1')