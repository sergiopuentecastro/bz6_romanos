import unittest
from romanos import *

class RomanosTest(unittest.TestCase):

    def test_single_simbol(self):
        self.assertEqual(romano_a_entero("M"), 1000)
        self.assertEqual(romano_a_entero("D"), 500)
        self.assertEqual(romano_a_entero("C"), 100)
        self.assertEqual(romano_a_entero("L"), 50)
        self.assertEqual(romano_a_entero("X"), 10)
        self.assertEqual(romano_a_entero("V"), 5)
        self.assertEqual(romano_a_entero("I"), 1)

        self.assertRaises(KeyError, romano_a_entero, "Z")
        self.assertRaises(ValueError, romano_a_entero, 23)

    def test_MMM (self):
        self.assertEqual(romano_a_entero("MMM"), 3000)

    def test_MMMM (self):
        self.assertRaises(OverflowError, romano_a_entero, "MMMM")

    def test_CC(self):
        self.assertEqual(romano_a_entero("CC"), 200)
    
    def test_III(self):
        self.assertEqual(romano_a_entero("III"), 3)

    def test_XX(self):
        self.assertEqual(romano_a_entero("XX"), 20)

    def test_VV(self):
        self.assertRaises(OverflowError, romano_a_entero, "VV")

    def test_repes_variadas(self):
        self.assertEqual(romano_a_entero("MMLXXIII"), 2073)

    def test_IV(self):
        self.assertEqual(romano_a_entero("IV"), 4)

    def test_IC(self):
        self.assertRaises(ValueError, romano_a_entero, "IC")



    if __name__ == "__main__":
        unittest.main()
