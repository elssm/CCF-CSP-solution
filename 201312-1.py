n = int(input())
nums = list(map(int,input().split()))
dict = {}
s = list(set(nums))
for i in s:
    dict[i] = nums.count(i)
s = max(dict,key=lambda k:dict[k])
print(s)