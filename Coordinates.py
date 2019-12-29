import random


class Coordinates:
    def __init__(self, row=None, column=None, length=None, direction=None):
        self.row = row
        self.column = column
        self.length = length
        self.direction = direction
        self.coordinates_list = self.generate_coordinates_list()

    def generate_random_row_and_column(self, max_coord):
        self.row = random.randint(0, max_coord - 1)
        self.column = random.randint(0, max_coord - 1)

    def generate_random_direction(self):
        self.direction = random.choice(["horizontal", "vertical"])

    def generate_random_coordinates(self, max_coord, length):
        while not self.is_valid_coordinates_list(max_coord):
            self.generate_random_row_and_column(max_coord)
            self.generate_random_direction()
            self.length = length
            self.coordinates_list = self.generate_coordinates_list()

    def generate_coordinates_list(self):
        if self.direction == "horizontal":
            coordinates_list = [
                {"row": self.row + x, "column": self.column}
                for x in range(int(self.length))
            ]
        elif self.direction == "vertical":
            coordinates_list = [
                {"row": self.row, "column": self.column + y}
                for y in range(int(self.length))
            ]
        else:
            coordinates_list = [{}]
        return coordinates_list

    def is_valid_row_and_column(self, max_len):
        is_valid = True
        if not (0 <= self.column <= max_len):
            is_valid = False
        elif not (0 <= self.row <= max_len):
            is_valid = False
        return is_valid

    def is_valid_coordinates_list(self, max_len):
        is_valid = True
        if len(self.coordinates_list) == 1:
            is_valid = False
        else:
            for i in self.coordinates_list:
                if i.get("row") > max_len or i.get("column") > max_len:
                    is_valid = False
                    break
        return is_valid

    def is_valid_coordinates_direction(self):
        is_valid = False
        for i in ["horizontal", "vertical"]:
            if self.direction == i:
                is_valid = True
        return is_valid

    def set_direction(self, user_direction):
        if user_direction.lower() == "v" or user_direction.lower() == "vertical":
            self.direction = "vertical"
        elif user_direction.lower() == "h" or user_direction.lower() == "horizontal":
            self.direction = "horizontal"
        else:
            raise ValueError("Invalid direction")

    def set_row_and_column(self, row, column, max_len):
        if row.isdigit() and column.isdigit():
            self.row = int(row)
            self.column = int(column)
            if not self.is_valid_row_and_column(max_len):
                raise ValueError("Invalid user coordinates")
        else:
            raise ValueError("Input must be numbers")

    def set_coordinates_manually(self, max_len):
        self.coordinates_list = self.generate_coordinates_list()
        if not self.is_valid_coordinates_list(max_len):
            raise ValueError("Ship coordinates out of range")
