import unittest
from romanos import *

class RomanosTest(unittest.TestCase):

    def test_descomponer(self):
        self.assertEqual(descomponer(1987), [1,9,8,7])

    def test_descomponer_solo_enteros(self):
        self.assertRaises(SyntaxError, descomponer, 1987.0)
    
    def test_convertir_987(self):
        self.assertEqual(convertir ([9,8,7]), "CMLXXXVII")

    def test_enetero_a_romano(self):
        self.assertEqual(entero_a_romano (1987), "MSMLXXXVII")
        self.assertRaises(OverflowError, entero_a_romano, 4000)
        self.assertRaises(OverflowError, entero_a_romano, 0)
