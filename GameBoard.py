import Coordinates


class GameBoard:
    def __init__(self, size):
        self.size = size
        self.board = self.generate_board()

    def generate_board(self):
        return [[0 for x in range(self.size)] for y in range(self.size)]

    def is_valid_ship_position(self, ship_coordinates):
        is_valid = True
        for i in ship_coordinates:
            if self.board[i.get("row")][i.get("column")] != 0:
                is_valid = False
                break
        return is_valid

    def add_ship(self, ship_coordinates, ship_length):
        for i in ship_coordinates:
            self.board[i.get("row")][i.get("column")] = ship_length

    def add_ships_randomly(self, ships):
        for i in ships:
            ship_added = False
            while not ship_added:
                ship_coordinates = Coordinates.Coordinates()
                ship_coordinates.generate_random_coordinates(self.size - 1, ships[i])
                if self.is_valid_ship_position(ship_coordinates.coordinates_list):
                    self.add_ship(ship_coordinates.coordinates_list, ships[i])
                    ship_added = True
                else:
                    ship_added = False

    def add_ships_manually(self, ships):
        print("Do you want to add ships (m)anually or (a)utomatically?")
        ship_generation = input()
        if ship_generation.lower() == "a":
            self.add_ships_randomly(ships)
        elif ship_generation.lower() == "m":
            for ship in ships:
                ship_added = False
                while not ship_added:
                    try:
                        user_ship_coordinates = Coordinates.Coordinates()
                        user_ship_coordinates.length = ships[ship]
                        user_ship_coordinates.set_row_and_column(
                            row=input(
                                f"Please write X coordinate for ship {ship}. It's size is: {ships[ship]}."
                                f" Max coordinate {self.size - 1} \r\n"
                            ),
                            column=input(
                                f"Please write Y coordinate for ship {ship}. It's size is: {ships[ship]}."
                                f" Max coordinate {self.size - 1} \r\n"
                            ),
                            max_len=self.size,
                        )
                        user_ship_coordinates.set_direction(
                            input(
                                f"Do you want to place ship (H)orizontally or (V)ertically? \r\n"
                            )
                        )
                        user_ship_coordinates.set_coordinates_manually(self.size)
                        if self.is_valid_ship_position(user_ship_coordinates.coordinates_list):
                            self.add_ship(user_ship_coordinates.coordinates_list, ships[ship])
                            ship_added = True
                        else:
                            raise ValueError("There already is ship in this position")
                    except ValueError as error:
                        print(error)
        else:
            self.add_ships_manually(ships)
        print("All ships added successfully")

    def print_board(self, show_ships=True):
        if show_ships:
            for i in self.board:
                print(i)
        else:
            for i in self.board:
                print([0 if x > 0 else x for x in i])
        print(
            "----------------------------------------------------------------------------"
        )

    def shoot(self, coordinates, who_shot):
        if who_shot == "computer":
            print(
                f"Computer shoots at: row {[coordinates.row]} and column {[coordinates.column]}"
            )
        if self.board[coordinates.row][coordinates.column] > 0:
            self.board[coordinates.row][coordinates.column] = -2
            print("Hit!")
        else:
            self.board[coordinates.row][coordinates.column] = -1
            print("Miss!")

    def validate_shot(self, coordinates):
        if not coordinates.is_valid_row_and_column(self.size):
            raise ValueError("Invalid shot. Shot coordinates not in range")
        elif self.board[coordinates.row][coordinates.column] < 0:
            raise ValueError("Invalid shot. You already shot there")

    def has_lost(self):
        has_lost = True
        for i in self.board:
            for j in i:
                if j > 0:
                    has_lost = False
                    break
        return has_lost

    def manual_shot(self, auto_play):
        if auto_play.lower() == "y":
            self.random_shot("user")
        else:
            has_shot = False
            while not has_shot:
                print("Write coordinates to shoot")
                shot_coordinates = Coordinates.Coordinates()
                try:
                    shot_coordinates.set_row_and_column(
                        row=input(
                            f"Please write X coordinate to shoot . Max coordinate {self.size - 1} \r\n"
                        ),
                        column=input(
                            f"Please write Y coordinate to shoot. Max coordinate {self.size - 1} \r\n"
                        ),
                        max_len=self.size,
                    )
                    self.validate_shot(shot_coordinates)
                    self.shoot(shot_coordinates, "user")
                    has_shot = True
                except ValueError as error:
                    print(error)

    def random_shot(self, who_shot):
        has_shot = False
        while not has_shot:
            try:
                computer_shot_coordinates = Coordinates.Coordinates()
                computer_shot_coordinates.generate_random_row_and_column(self.size)
                self.validate_shot(computer_shot_coordinates)
                self.shoot(computer_shot_coordinates, who_shot=who_shot)
                has_shot = True
            except ValueError as error:
                has_shot = False

    @staticmethod
    def get_board_plan():
        return {"Ship shot": -2, "Missed": -1, "Empty": 0}
