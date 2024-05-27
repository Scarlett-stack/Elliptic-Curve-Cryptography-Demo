from helper import run
from unittest import TestCase
from FieldElement import FieldElement
from Point import Point


class ECCTest(TestCase):

    def test_on_curve(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)
        valid_pts = ((192, 105), (17, 56), (1, 193))
        inv_pts = ((200, 119), (43, 99))
        for x_raw, y_raw in valid_pts:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            Point(x, y, a, b)
        for x_raw, y_raw in inv_pts:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            with self.assertRaises(ValueError):
                Point(x, y, a, b)

    def test_add(self):
        # tests the following additions on curve y^2=x^3-7 over F_223:
        # (192,105) + (17,56)
        # (47,71) + (117,141)
        # (143,98) + (76,66)
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)

        additions = (
            # (x1, y1, x2, y2, x3, y3)
            (192, 105, 17, 56, 170, 142),
            (47, 71, 117, 141, 60, 139),
            (143, 98, 76, 66, 47, 71),
        )

        # loop over additions
        # initialize x's and y's as FieldElements
        # create p1, p2 and p3 as Points
        # check p1+p2==p3
        for i in range(0, len(additions), 3):
            x1 = FieldElement(additions[i][0], prime)
            y1 = FieldElement(additions[i][1], prime)
            p1 = Point(x1, y1, a, b)
            x2 = FieldElement(additions[i][2], prime)
            y2 = FieldElement(additions[i][3], prime)
            p2 = Point(x2, y2, a, b)
            x3 = FieldElement(additions[i][4], prime)
            y3 = FieldElement(additions[i][5], prime)
            p3 = Point(x3, y3, a, b)
            assert p1 + p2 == p3, f"Failed for {p1} and {p2}, expected: {p3} got {p1 + p2}"
