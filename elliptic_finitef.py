from FieldElement import (FieldElement)
from Point import Point
prime = 223
a = FieldElement(num=0, prime=prime)
b = FieldElement(num=7, prime=prime)
x1 = FieldElement(num=47, prime=prime)
y1 = FieldElement(num=71, prime=prime)
x2 = FieldElement(num=60, prime=prime)
y2 = FieldElement(num=139, prime=prime)
p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)
print( p1 + p2)
for s in range(1,21):
    result = s*p1
    print('{}*(47,71)=({},{})'.format(s,result.x.num,result.y.num))
