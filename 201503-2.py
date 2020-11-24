m = map(int,input())
num = list(map(int,input().split()))
dict={}
num = sorted(num)
s=list(set(num))
for i in s:
    dict[i] = num.count(i)
l = sorted(dict.items(), key=lambda items:items[1], reverse=True)
for i in range(len(l)):
    print("{} {}".format(l[i][0],l[i][1]))
