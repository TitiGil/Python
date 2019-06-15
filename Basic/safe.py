
k=int(input())
code=input()
c=[]
for i in range(k):
    c.append(input())
    pass

def counter(num,ci):
    if ci.find(num)>(len(ci)-1)-ci.find(num):
        return len(ci)-ci.find(num)
    else:
        return ci.find(num)
count=0
for i in range(k):
    count+=counter(code[i],c[i])
    pass

print(count)

