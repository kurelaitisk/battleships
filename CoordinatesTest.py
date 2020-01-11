import unittest
from Coordinates import Coordinates


class CoordinatesTest(unittest.TestCase):
    @staticmethod
    def get_horizontal_coord_list():
        return [{"row": 0, "column": 0}, {"row": 1, "column": 0}, {"row": 2, "column": 0}, {"row": 3, "column": 0},
                {"row": 4, "column": 0}]

    @staticmethod
    def get_vertical_coord_list():
        return [{"row": 0, "column": 0}, {"row": 0, "column": 1}, {"row": 0, "column": 2}, {"row": 0, "column": 3},
                {"row": 0, "column": 4}]

    @staticmethod
    def get_valid_directions_list():
        return ["horizontal", "vertical"]

    def validate_row_and_column(self, max_coord, coordinates):
        self.assertGreaterEqual(coordinates.row, 0)
        self.assertLessEqual(coordinates.row, max_coord - 1)
        self.assertGreaterEqual(coordinates.column, 0)
        self.assertLessEqual(coordinates.column, max_coord - 1)

    def validate_direction(self, direction):
        self.assertIn(direction, self.get_valid_directions_list())

    def test_generate_coordinates_list_horizontal(self):
        test_coordinates = Coordinates(row=0, column=0, length=5, direction="horizontal")
        self.assertEqual(self.get_horizontal_coord_list(), test_coordinates.coordinates_list)

    def test_generate_coordinates_list_vertical(self):
        test_coordinates = Coordinates(row=0, column=0, length=5, direction="vertical")
        self.assertEqual(self.get_vertical_coord_list(), test_coordinates.coordinates_list)

    def test_generate_coordinates_list_empty(self):
        test_coordinates = Coordinates()
        self.assertEqual([{}], test_coordinates.coordinates_list)

    def test_generate_random_row_and_column(self):
        max_coord = 5
        test_coordinates = Coordinates()
        test_coordinates.generate_random_row_and_column(max_coord)
        self.validate_row_and_column(max_coord=max_coord, coordinates=test_coordinates)

    def test_generate_random_direction(self):
        test_coordinates = Coordinates()
        test_coordinates.generate_random_direction()
        self.validate_direction(test_coordinates.direction)

    def test_generate_random_coordinates(self):
        max_coord = 5
        length = 2
        test_coordinates = Coordinates()
        test_coordinates.generate_random_coordinates(max_coord=max_coord, length=length)

        self.validate_direction(test_coordinates.direction)
        self.validate_row_and_column(max_coord=max_coord, coordinates=test_coordinates)
        self.assertEqual(test_coordinates.length, length)
        self.assertIsNotNone(test_coordinates.coordinates_list)  # TO DO better test

    def test_is_valid_row_and_column(self):
        test_coordinates = Coordinates()
        max_coord = 10
        for i in range(10):
            test_coordinates.row = i
            test_coordinates.column = i
            self.assertTrue(test_coordinates.is_valid_row_and_column(max_len=max_coord))

    def test_is_valid_coordinates_list(self):
        test_coordinates = Coordinates()
        test_coordinates.coordinates_list = self.get_vertical_coord_list()
        self.assertTrue(test_coordinates.is_valid_coordinates_list(10))
        self.assertFalse(test_coordinates.is_valid_coordinates_list(3))
        test_coordinates.coordinates_list = self.get_horizontal_coord_list()
        self.assertTrue(test_coordinates.is_valid_coordinates_list(10))
        self.assertTrue(test_coordinates.is_valid_coordinates_list(4))
        test_coordinates.coordinates_list = [{"row": 0, "column": 0}]
        self.assertFalse(test_coordinates.is_valid_coordinates_list(10))

    def test_is_valid_coordinate_direction(self):
        test_coordinates = Coordinates()
        for i in self.get_valid_directions_list():
            test_coordinates.direction = i
            self.assertTrue(test_coordinates.is_valid_coordinates_direction())

        test_coordinates.direction = "invalidDirection"
        self.assertFalse(test_coordinates.is_valid_coordinates_direction())

    def test_set_row_and_column(self):
        test_coordinates = Coordinates()

        self.assertRaises(ValueError, lambda: test_coordinates.set_row_and_column(row="0", column="a", max_len=5))
        self.assertRaises(ValueError, lambda: test_coordinates.set_row_and_column(row="5", column="5", max_len=3))
        test_coordinates.set_row_and_column(row="5", column="5", max_len=5)
        self.assertEqual(test_coordinates.row, 5)
        self.assertEqual(test_coordinates.column, 5)

    def test_set_direction(self):
        test_coordinates = Coordinates()
        test_coordinates.set_direction("v")
        self.validate_direction(test_coordinates.direction)
        test_coordinates.set_direction("h")
        self.validate_direction(test_coordinates.direction)
        for i in self.get_valid_directions_list():
            test_coordinates.set_direction(i)
            self.validate_direction(test_coordinates.direction)


if __name__ == '__main__':
    unittest.main()
