import random


class Coordinates:
    def __init__(self, row=None, column=None, length=None, direction=None):
        self.row = row
        self.column = column
        self.length = length
        self.direction = direction
        self.coordinates_list = self.GenerateCoordinatesList()

    def GenerateRandomRowAndColumn(self, max_coord):
        self.row = random.randint(0, max_coord - 1)
        self.column = random.randint(0, max_coord - 1)

    def GenerateRandomDirection(self):
        self.direction = random.choice(["horizontal", "vertical"])

    def GenerateRandomCoordinates(self, max_coord, length):
        while not self.IsValid(max_coord):
            self.GenerateRandomRowAndColumn(max_coord)
            self.GenerateRandomDirection()
            self.length = length
            self.coordinates_list = self.GenerateCoordinatesList()

    def GenerateCoordinatesList(self):
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

    def IsValid(self, max_len):
        is_valid = True
        if len(self.coordinates_list) == 1:
            is_valid = False
        else:
            for i in self.coordinates_list:

                if i.get("row") > max_len or i.get("column") > max_len:
                    is_valid = False
                    break

        return is_valid

    def PrintCoordinates(self):
        for i in self.coordinates_list:
            print(i)

    def IsValidCoordDirection(self):
        is_valid = False
        for i in ["horizontal", "vertical"]:
            if self.direction == i:
                is_valid = True
        return is_valid

    def setDirection(self, user_direction):
        if user_direction.lower() == "v" or user_direction.lower() == "vertical":
            self.direction = "vertical"
        elif user_direction.lower() == "h" or user_direction.lower() == "horizontal":
            self.direction = "horizontal"
        else:
            raise ValueError("Invalid direction")

    def IsValidRowAndColumn(self, max_len):
        is_valid = True
        if not (0 <= self.column <= max_len):
            is_valid = False
        elif not (0 <= self.row <= max_len):
            is_valid = False
        return is_valid

    def setRowAndColumn(self, row, column, max_len):

        if row.isdigit() and column.isdigit():
            self.row = int(row)
            self.column = int(column)
            if not self.IsValidRowAndColumn(max_len):
                raise ValueError("Invalid user coordinates")
        else:
            raise ValueError("Input must be numbers")

    def SetUserCoords(self, max_len):
        self.coordinates_list = self.GenerateCoordinatesList()
        if not self.IsValid(max_len):
            raise ValueError("Ship coordinates out of range")