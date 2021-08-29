import unittest
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Love Shack", "The B-52's", 3.50)
        self.song2 = Song("I Got You Babe", "Sonny and Cher", 3.25)
        self.song3 = Song("Y.M.C.A", "The Village People", 4.00)

    def test_song_has_title(self):
        self.assertEqual("Y.M.C.A", self.song3.title)

        