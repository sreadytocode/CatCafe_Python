import unittest

class TestDrink(unittest.TestCase):
    pass

    def test_does_drink_has_a_name(self):
        self.assertEqual("Latte", self.drink.name)

    