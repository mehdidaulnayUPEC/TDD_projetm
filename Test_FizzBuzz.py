import unittest
from FizzBuzz import *

class Test_FizzBuzz(unittest.TestCase):

    def setUp(self):
        self.instance=FizzBuzz()


    def test_affiche(self):
        self.assertEqual(self.instance.affiche(5,10), "BuzzFizz78FizzBuzz")
        


if __name__ == '__main__':
    unittest.main()

