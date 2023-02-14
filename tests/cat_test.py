import unittest
from classes.cat import Cat

class TestCat(unittest.TestCase):

    def setUp(self):
        self.cat = Cat()
    
    def test_does_cat_have_a_name(self):
        self.assertEqual("Maya", self.cat.name)

    @unittest.skip("WIP")
    def test_does_cat_have_an_appetite(self):
        self.assertEqual(True, self.cat.appetite)