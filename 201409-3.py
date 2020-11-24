s1 = input()
flag=int(input())
n = int(input())
res=[]
for i in range(n):
    line = input()
    if flag == 1:
        if s1 in line:
            print(line)
    else:
        s1 = s1.lower()
        new_line = line.lower()
        if s1 in new_line:
            print(line)