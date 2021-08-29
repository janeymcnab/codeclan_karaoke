import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("No.1", ["Love Shack", "I Got You Babe", "Y.M.C.A"], 10, 15.00)
        self.room2 = Room("No.2", ["song4", "song5", "song6"], 15, 15.00)
        self.room3 = Room("No.3", ["song7", "song8", "song9"], 5, 15.00)

        self.song =Song("Believe", "Cher", 3.50)

        self.guest = Guest("Jane", 24, 150.00)

    def test_room_has_number(self):
        self.assertEqual("No.2", self.room2.number)   

    def test_room_has_song_list(self):
        self.assertEqual(["Love Shack", "I Got You Babe", "Y.M.C.A"], self.room.song_list)

    def test_check_in_guest(self):
        self.room.check_in_guests(self.guest)
        self.assertEqual(1, self.room.guest_count())

    def test_check_out_guest(self):
        self.room.check_out_guests
        self.assertEqual(0, self.room.guest_count())

    def test_add_song(self):
        self.assertEqual(["Love Shack", "I Got You Babe", "Y.M.C.A", "Believe"], self.room.add_song(self.song.title))

    def test_check_in_under_capacity(self):
        self.room3.check_in_guests(self.guest)
        self.room3.check_in_guests(self.guest)
        self.room3.check_in_guests(self.guest)
        self.room3.check_in_guests(self.guest)
        self.assertEqual(4, self.room3.guest_count())

    def test_check_in_over_capacity(self):
        self.room3.check_in_guests(self.guest)
        self.room3.check_in_guests(self.guest)
        self.room3.check_in_guests(self.guest)
        self.room3.check_in_guests(self.guest)
        self.room3.check_in_guests(self.guest)
        self.room3.check_in_guests(self.guest)
        self.assertEqual(5, self.room3.guest_count())

    def test_customer_payment(self):
        self.room3.check_in_guests(self.guest)
        self.assertEqual(15, self.room3.till)
        self.assertEqual(135.00, self.guest.wallet)
        



