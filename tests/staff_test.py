import unittest
from classes.staff import Staff

class TestStaff(unittest.TestCase):

    def setUp(self):
        self.staff = Staff()

    def test_does_staff_have_a_first_name(self):
        self.assertEqual("Mad", self.staff.first_name)

    @unittest.skip("WIP")
    def test_does_staff_have_last_name(self):
        self.assertEqual("Hatter", self.staff.last_name)

    @unittest.skip("WIP")
    def test_does_staff_have_a_role(self):
        self.assertEqual("Waitor", self.staff.role)