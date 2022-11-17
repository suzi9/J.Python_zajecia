import rectangles as rn
import unittest

class TestRectangle(unittest.TestCase): 
    def test__str__(self):
        self.assertEqual(str(rn.Rectangle(4, 5, 6, 7)), "[(4, 5), (6, 7)]")
        self.assertEqual(str(rn.Rectangle(3, 1, 10, 11)), "[(3, 1), (10, 11)]")
        self.assertEqual(str(rn.Rectangle(2, 14, 19, -99)), "[(2, 14), (19, -99)]")
        self.assertEqual(str(rn.Rectangle(0, 1, 6, 9)), "[(0, 1), (6, 9)]")
        self.assertEqual(str(rn.Rectangle(0, -3, 100, 15)), "[(0, -3), (100, 15)]")
    
    def test__repr__(self):
        self.assertEqual(repr(rn.Rectangle(2, 4, 34, 44)), "Rectangle(2, 4, 34, 44)")
        self.assertEqual(repr(rn.Rectangle(0, -99, 123, 83)), "Rectangle(0, -99, 123, 83)")
        self.assertEqual(repr(rn.Rectangle(-12, -2, 17, 20)), "Rectangle(-12, -2, 17, 20)")
        self.assertEqual(repr(rn.Rectangle(56, 53, -66, -31)), "Rectangle(56, 53, -66, -31)")
        self.assertEqual(repr(rn.Rectangle(73, 76, 118, 199)), "Rectangle(73, 76, 118, 199)")

    def test__eq__(self):
        self.assertEqual(rn.Rectangle(3, -2, 23, 14), rn.Rectangle(3, -2, 23, 14))
        self.assertEqual(rn.Rectangle(8, 23, 45, 51), rn.Rectangle(8, 23, 45, 51))
        self.assertEqual(rn.Rectangle(1, 7, 36, 22), rn.Rectangle(1, 7, 36, 22))
        self.assertEqual(rn.Rectangle(6, -4, 34, 66), rn.Rectangle(6, -4, 34, 66))
        self.assertEqual(rn.Rectangle(0, 0, 3, 9), rn.Rectangle(0, 0, 3, 9))

    def test__ne__(self):
        self.assertNotEqual(rn.Rectangle(-4, -6, 2, 7), rn.Rectangle(87, 54, 2222, 5675))
        self.assertNotEqual(rn.Rectangle(1, 5, 7221, 893), rn.Rectangle(4, 34, 111, 54839))
        self.assertNotEqual(rn.Rectangle(52, 22, 532, 9058), rn.Rectangle(-1, -2, 6, 7))
        self.assertNotEqual(rn.Rectangle(9, 3, 321, 1001), rn.Rectangle(64, 53, 432, 5273))
        self.assertNotEqual(rn.Rectangle(-65, -12, 556, 154), rn.Rectangle(83, 11, 29329, 3242))

    def test__center__(self):
        self.assertEqual(rn.Rectangle(1, 2, 5, 5).center(), rn.Point(2, 1.5))
        self.assertEqual(rn.Rectangle(5, 2, 9, 12).center(), rn.Point(2, 5))
        self.assertEqual(rn.Rectangle(0, 0, 9, 4).center(), rn.Point(4.5, 2))
        self.assertEqual(rn.Rectangle(10, 14, 56, 27).center(), rn.Point(23, 6.5))
        self.assertEqual(rn.Rectangle(12, 11, 783, 933).center(), rn.Point(385.5, 461))

    def test__area__(self):
        self.assertEqual(rn.Rectangle(2, 3, 4, 5).area(), 4)
        self.assertEqual(rn.Rectangle(11, 13, 56, 45).area(), 1440)
        self.assertEqual(rn.Rectangle(-2, -1, 47, 88).area(), 4361)
        self.assertEqual(rn.Rectangle(-15, -23, 745, 955).area(), 743280)
        self.assertEqual(rn.Rectangle(-35, -2, 854, 889).area(), 792099)

    def test__move__(self):
        self.assertEqual(rn.Rectangle(3, 2, 16, 73).move(6, 7), "[(9, 9), (22, 80)]")
        self.assertEqual(rn.Rectangle(-4, -1, 892, 100).move(4, 9), "[(0, 8), (896, 109)]")
        self.assertEqual(rn.Rectangle(0, 3, 12, 16).move(4, 2), "[(4, 5), (16, 18)]")
        self.assertEqual(rn.Rectangle(-5, -7, 24, 28).move(7, 10), "[(2, 3), (31, 38)]")
        self.assertEqual(rn.Rectangle(-10, -27, 8, 2).move(1, 2), "[(-9, -25), (9, 4)]")

if __name__ == '__main__':
    unittest.main()