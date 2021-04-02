# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 12 Practice 1
#
# Creates a 'name' class.
# -----------------------------------------------------------------------------

class Name:

    def __init__(self, first, last):
        if isinstance(first, str) and isinstance(last, str):
            self.first = first
            self.last = last
            self.nickname = None
        else:
            raise TypeError

    def get_first_name(self):
        return self.first

    def get_last_name(self):
        return self.last

    def get_full_name(self):
        return self.first + ' ' + self.last

    def set_nick_name(self, nick_name):
        if isinstance(nick_name, str):
            self.nickname = nick_name
        else:
            raise TypeError

    def get_nick_name(self):
        return self.nickname

    def __str__(self):
        if self.nickname == None:
            return self.first + ' ' + self.last
        else:
            return self.first + ' "' + self.nickname + '" ' + self.last


def main():
    my_name = Name('Jameson', 'Albers')
    print(my_name.get_first_name())
    print(my_name.get_last_name())
    print(my_name.get_full_name())
    print(my_name)
    my_name.set_nick_name('Friendo')
    print(my_name.get_nick_name())
    print(my_name)


main()