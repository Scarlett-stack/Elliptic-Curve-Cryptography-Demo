class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = "Num {} nu e bun trb doar intre 0 si {}".format(num, prime-1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return "Field element_{}({})".format(self.num, self.prime)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        if other is None:
            return False
        return self.num != other.num and self.prime == other.prime

    def __add__(self, other):
        print("din field el ", self.num, self.prime, other.num)
        if other.prime != self.prime:
            error = "NOT ADDING DIFF FIELDS"
            raise TypeError(error)
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if other.prime != self.prime:
            error = "cant work diffrent stuff"
            raise ValueError(error)
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if other.prime != self.prime:
            error = "no way"
            raise ValueError(error)
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exp):
        n = exp % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if  other.prime != self.prime:
            error = "brush"
            raise TypeError(error)
        num = self.num*pow(other.num, self.prime-2, self.prime) % self.prime
        return self.__class__(num, self.prime)

    def __rmul__(self, coefficient):
        num = (self.num * coefficient) % self.prime
        return self.__class__(num, self.prime)
"""
verific daca num apartine Field adica e intre 0 si prim-1
"""
a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)
print(a+b==c)
# print(a**3)
# print(a*b)
# print(a/b)
#print(a==b)
