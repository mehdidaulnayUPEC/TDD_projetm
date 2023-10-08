import unittest
from FizzBuzz import *

class Test_FizzBuzz(unittest.TestCase):

    def setUp(self):
        self.instance=FizzBuzz()


    def test_affiche(self):
        self.assertEqual(self.instance.affiche(15), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")
        


if __name__ == '__main__':
    unittest.main()

