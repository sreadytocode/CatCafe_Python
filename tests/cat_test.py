import unittest
from classes.cat import Cat

class TestCat(unittest.TestCase):

    def setUp(self):
        self.cat = Cat("Cheshire")
    
    def test_does_cat_have_a_first_name(self):
        self.assertEqual("Cheshire", self.cat.first_name)

    @unittest.skip("WIP")
    def test_does_cat_have_a_last_name(self):
        self.assertEqual("Cat", self.cat.last_name)

    @unittest.skip("WIP")
    def test_does_cat_have_an_appetite(self):
        self.assertEqual(True, self.cat.appetite)