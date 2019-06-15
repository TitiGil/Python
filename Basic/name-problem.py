n=int(input())
temp=[]
for i in range(n):
    temp.append(input())
    pass


def length(check):
    tname=[]
    for item in check:
        if item not in tname:
            tname.append(item)
            pass
        pass
    return len(tname)

max=0
for item in temp:
    if length(item)>max:
        max=length(item)
        pass
    pass


print(int(max))

