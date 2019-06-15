
import math
x=int(input())

rx=math.radians(x)
p1=math.ceil((x**(5/3))+(math.tan(rx)))
p2=math.floor(math.pi**(2+math.atan(math.pow(math.sin(rx),2))))

print(math.gcd(p1,p2))