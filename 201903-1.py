n = int(input())
nums = list(map(int,input().split()))
nums = sorted(nums)
ma = max(nums)
mi = min(nums)
if n % 2 != 0:
    mid = nums[n//2]
else:
    start = n//2-1
    end = start+1
    res = nums[start]+nums[end]
    if res%2==0:
        mid = res // 2
    else:
        mid = res / 2
print("{} {} {}".format(ma,mid,mi))