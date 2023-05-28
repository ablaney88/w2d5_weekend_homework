import unittest
from classes.rooms import Room
from classes.guests import Guest
from classes.songs import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Frank", 20.00)

    def test_decrease_wallet(self):
        self.guest.decrease_wallet(5.00)
        self.assertEqual(15.00, self.guest.wallet)