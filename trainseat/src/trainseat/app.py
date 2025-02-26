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

    position = seat_position()
    print(position)

    def startup(self):

        # Boxes
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.box1 = toga.Box(style=Pack(direction=ROW))
        self.box2 = toga.Box(style=Pack(direction=ROW))
        self.box3 = toga.Box(style=Pack(direction=COLUMN))


        # Elements
        self.label_enter_seat = toga.Label("Enter your ticket seat number: ")
        self.input_enter_seat = toga.TextInput()
        self.submit_button = toga.Button("submit", on_press=self.display_seat_position)
        self.your_seat_position = toga.Label("")
        self.show_canvas_button = toga.Button("show canvas", on_press=self.display_canvas)
        self.canvas = toga.Canvas(style=Pack(width=600, height=400))  # Set a size for the canvas !!! without no display of drawing

        # Elements dispatch to boxes
        self.box1.add(self.label_enter_seat,
                 self.input_enter_seat,
                 self.submit_button
                 )

        self.main_box.add(self.box1)
        self.main_box.add(self.box2)
        self.main_box.add(self.box3)


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
            self.box2.add(self.show_canvas_button)
        except ValueError:
            self.box2.remove(self.your_seat_position)
            self.your_seat_position = toga.Label(f'"{self.input_enter_seat.value}" is not a seat number. Check your seat number on the ticket.')
            self.box2.add(self.your_seat_position)

    def draw_seat_square(self, upper_left_x, upper_left_y, sq_side_size):
        self.context = self.canvas.context
        self.context.begin_path()
        # line to right
        self.context.move_to(upper_left_x, upper_left_y)
        self.context.line_to(upper_left_x + sq_side_size, upper_left_y)
        # line down
        self.context.line_to(upper_left_x + sq_side_size, upper_left_y + sq_side_size )
        # line left
        self.context.line_to(upper_left_x, upper_left_y + sq_side_size)
        # line up close
        self.context.line_to(upper_left_x, upper_left_y)
        self.context.stroke(color="red")


    def display_canvas(self, widget):
        self.box3.add(self.canvas)
        self.draw_seat_square(50, 100, 100)


def main():
    return trainseat()







