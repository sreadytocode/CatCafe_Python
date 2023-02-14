import unittest

class TestDrink(unittest.TestCase):
    pass

    def test_does_drink_has_a_name(self):
        self.assertEqual("Latte", self.drink.name)

    @unittest.skip("WIP")
    def test_does_drink_has_a_price(self):
        self.assertEquals(3.20, self.drink.price)