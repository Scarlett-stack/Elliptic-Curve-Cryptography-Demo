# Elliptic-Curve-Cryptography-Demo
Python code for checking Point Addition, Scalar Multiplication and Division <br>
Testing module (don't rely on it though) : ECCTest.py
How tp run? Note that if you run it like this you don't need to import the FieldElement class
```
python3 <filename>.py
```
First we implement the FieldElement class for checking if an element belongs in the field Fprime
The output should look like this: <br>
```
>>> from ecc import FieldElement
>>> a = FieldElement(7, 13)
>>> b = FieldElement(6, 13)
>>> print(a == b)
False
>>> print(a == a)
True
```
(now go look at the code for comments and details)
We also need addition and substraction for elements belonging in the same Field. Multiplication is handled using modulo for getting our result back in our Field<sub>prime</sub>
So what's up with division? Why the self.prime - 2? <br>
Because division is inverse of multipication we can write a/b as a *b ^(-1). Using Fermat's little theorem : <BR>
b<sup>p-1</sup> = 1, because p is prime
<br>
<!-- b<sup>-1</sup> = b ^(-1) * 1 = b^(-1) * b^(p-1) =  b ^ (p-2) r b ^(-1) = b ^(p-2) -->
 b<sup>-1</sup> * 1 = b<sup>-1</sup> * b<sup>p-1</sup> = b<sup>p-2</sup>
<br>
Rmul (real multiplication) handles negative exponents as well.
ok that's it with FieldElement

