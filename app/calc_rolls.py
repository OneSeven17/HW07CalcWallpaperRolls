def calculate_roll_quantity (room_length, room_width, room_height, roll_width, roll_length):

    perimeter = room_length * 2 + room_width * 2
    strip_quantity = round(perimeter / roll_width + 0.5)  # the result will not be true, if the result of the division is an integer
    strip_quantity_in_roll = roll_length / (room_height + 10)
    roll_quantity = round(strip_quantity / strip_quantity_in_roll + 0.5)  # the result will not be true, if the result of the division is an integer

    return roll_quantity