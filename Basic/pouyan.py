p, d = map(int, input().split())

x=1
while ((x*d)%p)>(p/2):
    x+=1
    pass
print(x*d)    

