class Room:
    def __init__(self, room_name, till, capacity, song_list):
        self.room_name = room_name
        self.till = till
        self.capacity = capacity
        self.song_list = song_list
        self.rooms = []
        self.song = []


    def check_guest_in(self, guest):
        self.capacity += guest

    def check_guest_out(self, guest):
        self.capacity -= guest

    def add_song(self, song):
        self.song_list += song

    def remove_song(self, song):
        self.song_list -= song

    def increase_till(self, amount):
        self.till += amount

    def room_is_full(self, guest_number):
        if guest_number > 4:
            return "Sorry! the room is full. Find somewhere else to sing"
        elif guest_number < 4:
            return "Come on in!"



