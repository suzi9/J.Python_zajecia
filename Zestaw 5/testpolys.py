import unittest
import polys as P

class TestPolynomials(unittest.TestCase):

    def setUp(self):
       self.p1 = [2, 1]                   # W(x) = 2 + x
       self.p2 = [2, 1, 0]                # jw  (niejednoznaczność)
       self.p3 = [-3, 0, 1]               # W(x) = -3 + x^2
       self.p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
       self.p5 = [0]                      # zero
       self.p6 = [0, 0, 0]                # zero (niejednoznaczność)

    def test_add_poly(self):
        self.assertEqual(P.add_poly(self.p1, self.p2), [4, 2, 0])
        self.assertEqual(P.add_poly(self.p2, self.p3), [-1, 1, 1])

    def test_sub_poly(self):
        self.assertEqual(P.sub_poly(self.p2, self.p1), [0, 0, 0])
        self.assertEqual(P.sub_poly(self.p1, self.p3), [5, 1, -1, 0])

    def test_mul_poly(self): 
        self.assertEqual(P.mul_poly(self.p3, self.p2), [-6, -3, 2, 1, 0])
        self.assertEqual(P.mul_poly(self.p4, self.p5), [0])

    def test_is_zero(self): 
        self.assertFalse(P.is_zero(self.p3))
        self.assertFalse(P.is_zero(self.p4))
        self.assertTrue(P.is_zero(self.p5))
        self.assertTrue(P.is_zero(self.p6))

    def test_eq_poly(self): 
        self.assertFalse(P.eq_poly(self.p4, self.p1))
        self.assertTrue(P.eq_poly(self.p5, self.p6))

    def test_eval_poly(self):
        self.assertEqual(P.eval_poly(self.p1, 4), 9)
        self.assertEqual(P.eval_poly(self.p2, 8), 136)

    def test_combine_poly(self): 
        self.assertEqual(P.combine_poly(self.p2, self.p3), [-1, 0, 1, 0, 0])
        self.assertEqual(P.combine_poly(self.p4, self.p1), [3, 0])

    def test_pow_poly(self): 
        self.assertEqual(P.pow_poly(self.p2, 6), [64, 192, 240, 160, 60, 12, 1, 0, 0, 0, 0, 0, 0])
        self.assertEqual(P.pow_poly(self.p3, 5), [-243, 0, 405, 0, -270, 0, 90, 0 , -15, 0, 1])

    def test_diff_poly(self): 
        self.assertEqual(P.diff_poly(self.p1), [0, 1])
        self.assertEqual(P.diff_poly(self.p2), [0, 1, 0])

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy