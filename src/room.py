class Room:
    def __init__(self, number, song_list, capacity, cost):
        self.number = number
        self.song_list = song_list
        self.guest_list = []
        self.capacity = capacity
        self.cost = cost
        self.till = 0

    def guest_count(self):
        return len(self.guest_list)

    def check_in_guests(self, guest):
        if len(self.guest_list) < self.capacity and guest.wallet >= self.cost:
            self.guest_list.append(guest)
            self.till += self.cost
            guest.wallet -= self.cost

        

    def check_out_guests(self, guest):
        self.guest_list.remove(guest)
        
    def add_song(self, song):
        self.song_list.append(song)
        return self.song_list



