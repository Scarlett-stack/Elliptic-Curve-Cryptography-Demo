class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0: #check if number is between 0 and num -1 inclusive
            error = "Num {} nu e bun trb doar intre 0 si {}".format(num, prime-1)
            raise ValueError(error) #it's not thus raise ValuError()
        self.num = num #otherwise just assign for the current object the value (input) and the prime
        self.prime = prime #over which we defined our field

    def __repr__(self):
        return "Field element_{}({})".format(self.num, self.prime)

    def __eq__(self, other):    #overloading of == operator , checks if two FieldElement objects are equal
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime  #check attributes

    def __ne__(self, other):    #overloading for !=
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
        n = exp % (self.prime - 1)  #force the exponent back in our field
        num = pow(self.num, n, self.prime)  #use modulo self.prime (3rd argument) to reduce here as well
        return self.__class__(num, self.prime)

    def __truediv__(self, other): #inverse of multiplication
        if  other.prime != self.prime: #i can't operate in diffrent fields !
            error = "brush"
            raise TypeError(error)
        num = self.num*pow(other.num, self.prime-2, self.prime) % self.prime
        return self.__class__(num, self.prime)

    def __rmul__(self, coefficient): #for negative exponents!
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
