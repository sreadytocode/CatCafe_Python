import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def test_does_guest_have_a_first_name(self):
        self.assertEqual("Sara", self.guest.first_name)