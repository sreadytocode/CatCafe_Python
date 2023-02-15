import unittest
from classes.cafe import Cafe
from classes.drink import Drink

class TestCafe(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drink("Latte", 3.50)
        self.drink_2 = Drink("Earl Grey Tea", 3.50)

        self.cafe = Cafe("Wonderland", 500.00)
        

    def test_does_cafe_have_a_name(self):
        self.assertEqual("Wonderland", self.cafe.name)

    # @unittest.skip("WIP")
    def test_does_cafe_have_a_till(self):
        self.assertEqual(500.00, self.cafe.till)

    # @unittest.skip("WIP")
    def test_does_cafe_drink_stock_value_start_at_0(self):
        self.assertEqual(0, self.cafe.drink_stock_value())
    
    # @unittest.skip("WIP")
    def test_drink_stock_level_0_if_drink_not_in_stock(self):
        self.assertEqual(0, self.cafe.drink_stock_level(self.drink_1))

    # @unittest.skip("WIP")
    def test_cafe_can_add_drink(self):
        self.cafe.add_drink(self.drink_2)
        self.assertEqual(1, self.cafe.drink_stock_level(self.drink_2))
        self.assertEqual(3.50, self.cafe.drink_stock_value())

    def test_cafe_can_add_multiple_drinks(self):
        self.cafe.add_drink(self.drink_1)
        self.cafe.add_drink(self.drink_1)
        self.assertEqual(2, self.cafe.drink_stock_level(self.drink_1))
        self.assertEqual(7.00, self.cafe.drink_stock_value())

