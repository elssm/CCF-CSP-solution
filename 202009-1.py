n,x,y = map(int,input().split())
res = []
dict = {}
for i in range(n):
    num = list(map(int,input().split()))
    res.append(num)
for i in range(n):
    x1 = x-res[i][0]
    y1 = y-res[i][1]
    dict[i+1] = pow(x1,2)+pow(y1,2)
resort = sorted(dict.items(),key=lambda dict:dict[1]) #根据字典的值排序
# print(dict)
# print(sorted(dict.items(),key=lambda dict:dict[1])) 
for i in range(3):
    print(resort[i][0])


