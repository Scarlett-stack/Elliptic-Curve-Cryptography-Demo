from FieldElement import FieldElement

class Point:

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError('({}, {}) is not on the curve'.format(x, y))
    # end::source1[]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        # this should be the inverse of the == operator
        return not (self == other)

    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        elif isinstance(self.x, FieldElement):
            return 'Point({},{})_{}_{} FieldElement({})'.format(
                self.x.num, self.y.num, self.a.num, self.b.num, self.x.prime)
        else:
            return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}, {} are not on the same curve'.format(self, other))
        # Case 0.0: self is the point at infinity, return other
        if self.x is None:
            return other
        # Case 0.1: other is the point at infinity, return self
        if other.x is None:
            return self

        # Case 1: self.x == other.x, self.y != other.y
        # Result is point at infinity
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)

        # Case 2: self.x ≠ other.x
        # Formula (x3,y3)==(x1,y1)+(x2,y2)
        # s=(y2-y1)/(x2-x1)
        # x3=s**2-x1-x2
        # y3=s*(x1-x3)-y1
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = s**2 - self.x - other.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

        # Case 4: if we are tangent to the vertical line,
        # we return the point at infinity
        # note instead of figuring out what 0 is for each type
        # we just use 0 * self.x
        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)

        # Case 3: self == other
        # Formula (x3,y3)=(x1,y1)+(x1,y1)
        # s=(3*x1**2+a)/(2*y1)
        # x3=s**2-2*x1
        # y3=s*(x1-x3)-y1
        if self == other:
            s = (3 * self.x**2 + self.a) / (2 * self.y)
            x = s**2 - 2 * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)
    def __rmul__(self, coefficient):
        coef = coefficient
        current = self  # <1>
        result = self.__class__(None, None, self.a, self.b)  # <2>
        while coef:
            if coef & 1:  # <3>
                result += current
            current += current  # <4>
            coef >>= 1  # <5>
        return result
# class Point:
#
#     def __init__(self, x, y, a, b):
#         self.x = x
#         self.y = y
#         self.a = a
#         self.b = b
#         if self.x is None and self.y is None:
#             return
#         print("din point: x , y, a ,b", self.x**3, self.y**2, a, b)
#         if self.y**2 != self.x**3 + a * x + b:
#             raise ValueError('({}, {}) IS NOT ON THE CURVE'.format(x, y))
#
#     def __eq__(self, other):
#         if self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.a:
#             return True
#         else:
#             return False
#
#     def __ne__(self, other):
#         return not (self == other) #use overloading
#
#     def __repr__(self):
#         if self.x is None:
#             return 'Point(infinity)'
#         elif isinstance(self.x, FieldElement):
#             return 'Point({},{})_{}_{} FieldElement({})'.format(
#                 self.x.num, self.y.num, self.a.num, self.b.num, self.x.prime)
#         else:
#             return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)
#
#     def __add__(self, other):
#         if self.a != other.a or self.b != other.b:
#             raise TypeError("Points {} and {} not on the same curve".format(self,other))
#         if self.x is None:
#             return other
#         if other.x is None:
#             return self
#
#         if other.x == self.x and other.y != self.y:
#             return self.__class__(None, None, self.a, self.b)
#         if self.x != other.x:
#             s = (other.y - self.y)/(other.x - self.x)
#             x3 = s**2 - self.x - other.x
#             y3 = s*(self.x - x3) - self.y #nue other.x e x3!!
#             return self.__class__(x3, y3, self.a, self.b)
#         if self == other and self.y == 0:
#             return self.__class__(None, None, self.a, self.b)
#         if self == other:
#             s_spec = (3*self.x**2 + self.a)/(2*self.y)
#             x3 = s_spec**2 - 2*self.x
#             y3 = s_spec*(self.x - x3)-self.y
#             return self.__class__(x3, y3, self.a, self.b)
#     def __rmul__(self, coefficient):
#         coef = coefficient
#         current = self  # <1>
#         print("cat e coef: ", coefficient)
#         result = self.__class__(None, None, self.a, self.b)  # <2>
#         while coef:
#             if coef & 1:  # <3>
#                 result += current
#                 print("rmul x si y ", result.x, result.y)
#             current =current + current  # <4>
#             coef >>= 1  # <5>
#         return result
# p1 = Point(-1,-1,5,7)
# p2 = Point(2,4,5,7)
# a = Point(x=3, y=-7, a=5, b=7)
# b = Point(x=18, y=77, a=5, b=7)
prime = 223
a = FieldElement(0,prime)
b = FieldElement(7, prime)
x = FieldElement(15, prime)
y = FieldElement(86, prime)
p = Point(x,y,a,b)
print(7*p)