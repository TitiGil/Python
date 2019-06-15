
a=input()
b=input()
c=input()
result=""
import re

if "#" in c:
    temp=str(int(a)+int(b))
    if c[-1]=="#" or c[0]=="#":
        c=c.replace("#", "")
        if c in temp:
            result="%s+%s=%s" %(a,b,temp)
            pass
        else:
            result="-1"
            pass
        pass
    else:
        c=c.split("#")
        st=("%s\d+%s") %(c[0],c[1])
        if len(re.findall(st,temp))!=0:
            result="%s+%s=%s" %(a,b,temp)
            pass
        else:
            result="-1"
            pass
        pass

    pass
elif "#" in a:
    temp=str(int(c)-int(b))
    if a[-1]=="#" or a[0]=="#":
        a=a.replace("#", "")
        if a in temp:
            result="%s+%s=%s" %(temp,b,c)
            pass
        else:
            result="-1"
            pass
        pass
    else:
        a=a.split("#")
        st=("%s\d+%s") %(a[0],a[1])
        if len(re.findall(st,temp))!=0:
            result="%s+%s=%s" %(temp,b,c)
            pass
        else:
            result="-1"
            pass
        pass

    pass
else:
    temp=str(int(c)-int(a))
    if b[-1]=="#" or b[0]=="#":
        b=b.replace("#", "")
        if b in temp:
            result="%s+%s=%s" %(a,temp,c)
            pass
        else:
            result="-1"
            pass
        pass
    else:
        b=b.split("#")
        st=("%s\d+%s") %(b[0],b[1])
        if len(re.findall(st,temp))!=0:
            result="%s+%s=%s" %(a,temp,c)
            pass
        else:
            result="-1"
            pass
        pass

    pass

print(result)
