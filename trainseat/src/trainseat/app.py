"""
app that shows seat in train location
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def seat_position(seat=1):
    window_seats = []
    for num in range(1, 55):
        if num % 6 == 0:
            window_seats.append(num - 5)
            window_seats.append(num)

    middle_seats = []
    for num in range(1, 55):
        if (num - 2) % 3 == 0:
            middle_seats.append(num)
    edge_seats = []
    for num in range(3, 55, 6):
        edge_seats.append(num)
        edge_seats.append(num + 1)

    if seat in window_seats:
        return "You have window seat"
    elif seat in middle_seats:
        return "You have middle seat"
    elif seat in edge_seats:
        return "You have edge seat"
    else:
       return "Wrong number. Check your seat number on the ticket."



class trainseat(toga.App):

    # position = seat_position()
    # print(position)

    def startup(self):

        # Boxes
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.box1 = toga.Box(style=Pack(direction=ROW))
        self.box2 = toga.Box(style=Pack(direction=ROW))

        # Elements
        self.label_enter_seat = toga.Label("Enter your ticket seat number: ")
        self.input_enter_seat = toga.TextInput()
        self.submit_button = toga.Button("submit", on_press=self.display_seat_position)

        self.your_seat_position = toga.Label("")


        # Elements dispatch to boxes
        self.box1.add(self.label_enter_seat,
                 self.input_enter_seat,
                 self.submit_button
                 )
        self.main_box.add(self.box1)

        self.box2.add(self.your_seat_position)
        self.main_box.add(self.box2)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()


    def display_seat_position(self, widget):
        try:
            seat = int(self.input_enter_seat.value)
            position = seat_position(seat)
            self.box2.remove(self.your_seat_position)
            self.your_seat_position = toga.Label(position)
            self.box2.add(self.your_seat_position)
        except ValueError:
            self.box2.remove(self.your_seat_position)
            self.your_seat_position = toga.Label(f'"{self.input_enter_seat.value}" is not a seat number. Check your seat number on the ticket.')
            self.box2.add(self.your_seat_position)



def main():
    return trainseat()







