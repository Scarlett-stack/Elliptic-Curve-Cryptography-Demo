from FieldElement import FieldElement
from Point import Point
prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)
x = FieldElement(47, prime)
y = FieldElement(71, prime)
p = Point(x, y, a, b)
for s in range(1, 21):
    result = s*p
    print('{}*(47,71)=({},{})'.format(s, result.x.num, result.y.num))
