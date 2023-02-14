import unittest
from classes.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Latte")

    def test_does_drink_has_a_name(self):
        self.assertEqual("Latte", self.drink.name)

    @unittest.skip("WIP")
    def test_does_drink_has_a_price(self):
        self.assertEquals(3.20, self.drink.price)