import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Jane", 24, 150.00)
        self.guest2 = Guest("Andrew", 31, 30.00)
        self.guest3 = Guest("Martin", 31, 30.00)
        self.guest4 = Guest("Eve", 27, 20.00)

    def test_guest_has_name(self):
        self.assertEqual("Eve", self.guest4.name)

    def test_guest_has_age(self):
        self.assertEqual(31, self.guest3.age)