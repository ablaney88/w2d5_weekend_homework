import unittest
from classes.rooms import Room
from classes.guests import Guest
from classes.songs import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        # self.room = Room("Codeclan Caraoke", 0)
        self.room1 = Room("Emo Lounge", 50.00, 0, 0)
        self.room2 = Room("Metal Lounge", 75.00, 1, 1)
        self.guest1 = Guest("Frank", 20.00)
        self.guest2 = Guest("Clare", 15.00)
        self.guest3 = Guest("Matt", 10.00)
        self.guest4 = Guest("Rachel", 45.00)
        self.song1 = Song("The quiet things that no one ever knows")
        self.song2 = Song("Playing God")


    # def test_caraoke_bar_has_name(self):
    #     self.assertEqual("Codeclan Caraoke", self.room.room_name)

    def test_guest_checks_in(self):
        self.room1.check_guest_in(1)
        self.assertEqual(1, self.room1.capacity)

    def test_guest_checks_out(self):
        self.room2.check_guest_out(1)
        self.assertEqual(0, self.room2.capacity)

    def test_add_song_to_list(self):
        self.room1.add_song(1)
        self.assertEqual(1, self.room1.song_list)

    def test_remove_song_from_list(self):
        self.room2.remove_song(1)
        self.assertEqual(0, self.room2.song_list)

    def test_room_has_till_value(self):
        self.assertEqual(50.00, self.room1.till)

    def test_increase_till(self):
        self.room1.increase_till(5.50)
        self.assertEqual(55.50, self.room1.till)

    def test_room_is_full(self):
        self.assertEqual("Sorry! the room is full. Find somewhere else to sing", self.room1)


