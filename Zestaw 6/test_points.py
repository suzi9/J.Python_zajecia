import unittest
import points as ptt

class TestPoint(unittest.TestCase): 
    
    def test__str__(self):
       self.assertEqual(str(ptt.Point(63, 23)), "(63, 23)")
       self.assertEqual(str(ptt.Point(21, 93)), "(21, 93)")
       self.assertEqual(str(ptt.Point(1, 4)), "(1, 4)")
       self.assertEqual(str(ptt.Point(243, 5)), "(243, 5)")
       self.assertEqual(str(ptt.Point(1892, 238342)), "(1892, 238342)")
    
    def test__repr__(self):
        self.assertEqual(repr(ptt.Point(3, 81)), "Point(3, 81)")
        self.assertEqual(repr(ptt.Point(73, 1231)), "Point(73, 1231)")
        self.assertEqual(repr(ptt.Point(-9, 0)), "Point(-9, 0)")
        self.assertEqual(repr(ptt.Point(72, -101)), "Point(72, -101)")
        self.assertEqual(repr(ptt.Point(8, 22)), "Point(8, 22)")

    def test__eq__(self):
        self.assertEqual(ptt.Point(4, 3), ptt.Point(4, 3))
        self.assertEqual(ptt.Point(7, -90), ptt.Point(7, -90))
        self.assertEqual(ptt.Point(43, 12), ptt.Point(43, 12))
        self.assertEqual(ptt.Point(-590, -1), ptt.Point(-590, -1))
        self.assertEqual(ptt.Point(0, 1), ptt.Point(0, 1))

    def test__ne__(self):
        self.assertNotEqual(ptt.Point(45, -3), ptt.Point(2, -1))
        self.assertNotEqual(ptt.Point(-971, 231), ptt.Point(79, -84))
        self.assertNotEqual(ptt.Point(326, 11), ptt.Point(50, 342))
        self.assertNotEqual(ptt.Point(57, 76), ptt.Point(3, -7))
        self.assertNotEqual(ptt.Point(0, 1223), ptt.Point(0, 0))

    def test__add__(self):
        self.assertEqual(ptt.Point(5, 2) + ptt.Point(-1, 8), ptt.Point(4, 10))
        self.assertEqual(ptt.Point(34, -8) + ptt.Point(12, 54), ptt.Point(46, 46))
        self.assertEqual(ptt.Point(-76, -2) + ptt.Point(0, 345), ptt.Point(-76, 343))
        self.assertEqual(ptt.Point(-574, -327) + ptt.Point(452, 10), ptt.Point(-122, -317))
        self.assertEqual(ptt.Point(5473, 43) + ptt.Point(-15, 7), ptt.Point(5458, 50))

    def test__sub__(self):
        self.assertEqual(ptt.Point(7, -87) - ptt.Point(4, 3), ptt.Point(3, -90))
        self.assertEqual(ptt.Point(-47, 0) - ptt.Point(-34, 22), ptt.Point(-13, -22))
        self.assertEqual(ptt.Point(7,  7) - ptt.Point(-4, -18), ptt.Point(11, 25))
        self.assertEqual(ptt.Point(0, -9) - ptt.Point(342, 2), ptt.Point(-342, -11))
        self.assertEqual(ptt.Point(1, -66)- ptt.Point(767, 0), ptt.Point(-766, -66))
    
    def test__mul__(self):
        self.assertEqual(ptt.Point(9, 34) * ptt.Point(76, -3), 582)
        self.assertEqual(ptt.Point(-30, 12) * ptt.Point(6, -53), -816)
        self.assertEqual(ptt.Point(54, -65) * ptt.Point(-1, -3), 141)
        self.assertEqual(ptt.Point(545, 304) * ptt.Point(42, 11), 26234)
        self.assertEqual(ptt.Point(55, 209) * ptt.Point(7, 5), 1430)

    def test__cross__(self):
        self.assertEqual(ptt.Point(9, 6).cross(ptt.Point(-8, 2)), 66)
        self.assertEqual(ptt.Point(7, 0).cross(ptt.Point(5, 3)), 21)
        self.assertEqual(ptt.Point(67, 1).cross(ptt.Point(7, 47)), 3142)
        self.assertEqual(ptt.Point(0, 0).cross(ptt.Point(-3, -9)), 0)
        self.assertEqual(ptt.Point(-77, 5).cross(ptt.Point(-7, 0)), 35)

    def test__length__(self):
        self.assertEqual(ptt.Point(7, 4).length(), 8.06225774829855)
        self.assertEqual(ptt.Point(0, 4).length(), 4)
        self.assertEqual(ptt.Point(1, 2).length(), 2.23606797749979)
        self.assertEqual(ptt.Point(8, 7).length(), 10.63014581273465)
        self.assertEqual(ptt.Point(6, 6).length(), 8.48528137423857)

    def test__hash__(self):
        self.assertEqual(hash(ptt.Point(9, 4)), 3556319275019275711)
        self.assertEqual(hash(ptt.Point(-7, 3)), 6626409277243510517)
        self.assertEqual(hash(ptt.Point(1, 1)), 8389048192121911274)
        self.assertEqual(hash(ptt.Point(21, 5)), -7293923049018386988)
        self.assertEqual(hash(ptt.Point(13, 2)), 3208945455351120664)


if __name__ == '__main__':
    unittest.main()