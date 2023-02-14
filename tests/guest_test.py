import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Alice", "Liddell", 50.00)
    
    def test_does_guest_have_a_first_name(self):
        self.assertEqual("Alice", self.guest.first_name)

    # @unittest.skip("WIP")
    def test_does_guest_have_a_last_name(self):
        self.assertEqual("Liddell", self.guest.last_name)

    # @unittest.skip("WIP")
    def test_does_guest_have_cash(self):
        self.assertEqual(50.00, self.guest.wallet)