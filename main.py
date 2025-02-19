# General idea
# When travel with tran 3rd class there is always question where is my seat? Is at window or not?
# This off course can be adjusted during buy process, but let's say you forgot.
# Make small app that could be run on multiple platforms mobile android
# that can tell you where is your seat: is at window, in the middle or at passage
# For layout of seats in train see picture in train layout.png and coupe numbering logic in coupe layout.png

# Perhaps it's possible to make app that shows your seat on the picture coupe blank.png??

def seat_position(seat):

    window_seats = []
    for num in range (1,55):
       if num % 6 == 0:
           window_seats.append(num - 5)
           window_seats.append(num)

    middle_seats = []
    for num in range (1,55):
        if (num-2)%3 ==  0:
            middle_seats.append(num)

    if seat in window_seats:
        print("You have window seat")
    elif seat in middle_seats:
        print("You have middle seat")
    else:
        print("You have edge seat")

seat_position(23)