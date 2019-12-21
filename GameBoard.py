import Coordinates


class GameBoard:
    def __init__(self, size):
        self.size = size
        self.board = GameBoard.GenerateBoard(size)

    @staticmethod
    def GenerateBoard(size):
        return [[0 for x in range(size)] for y in range(size)]

    def IsValidShipPosition(self, ship_coordinates):
        is_valid = True
        for i in ship_coordinates:
            if self.board[i.get("row")][i.get("column")] != 0:
                is_valid = False
                break
        return is_valid

    def AddShip(self, ship_coordinates, ship_length):
        for i in ship_coordinates:
            self.board[i.get("row")][i.get("column")] = ship_length
        # raise ValueError('You already have ship in this position')

    def AddComputerShips(self, ships):

        for i in ships:
            ship_added = False
            while not ship_added:
                ship_coordinates = Coordinates.Coordinates()
                ship_coordinates.GenerateRandomCoordinates(self.size - 1, ships[i])
                if self.IsValidShipPosition(ship_coordinates.coordinates_list):
                    self.AddShip(ship_coordinates.coordinates_list, ships[i])
                    ship_added = True
                else:
                    ship_added = False

    def AddUserShips(self, ships):

        print("Do you want to add ships (m)anually or (a)utomatically?")
        ship_generation = input()
        if ship_generation.lower() == "a":
            self.AddComputerShips(ships)
        elif ship_generation.lower() == "m":
            for ship in ships:
                ship_added = False
                while not ship_added:
                    try:
                        user_ship_coordinates = Coordinates.Coordinates()
                        user_ship_coordinates.length = ships[ship]
                        user_ship_coordinates.setRowAndColumn(
                            row=input(
                                f"Please write X coordinate for ship {ship}. It's size is: {ships[ship]}. Max coordinate {self.size - 1} \r\n"
                            ),
                            column=input(
                                f"Please write Y coordinate for ship {ship}. It's size is: {ships[ship]}. Max coordinate {self.size - 1} \r\n"
                            ),
                            max_len=self.size,
                        )
                        user_ship_coordinates.setDirection(
                            input(
                                f"Do you want to place ship (H)orizontally or (V)ertically? \r\n"
                            )
                        )
                        user_ship_coordinates.SetUserCoords(self.size)
                        if self.IsValidShipPosition(
                            user_ship_coordinates.coordinates_list
                        ):
                            self.AddShip(
                                user_ship_coordinates.coordinates_list, ships[ship]
                            )
                            ship_added = True
                        else:
                            raise ValueError("There already is ship in this position")
                    except ValueError as error:
                        print(error)
        else:
            self.AddUserShips(ships)
        print("All ships added")

    def PrintBoard(self, show_ships=True):
        if show_ships:
            for i in self.board:
                print(i)
        else:
            for i in self.board:
                print([0 if x > 0 else x for x in i])
        print(
            "----------------------------------------------------------------------------"
        )

    def Shoot(self, coordinates, who_shot):
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

    def ValidateShot(self, coordinates):
        if not coordinates.IsValidRowAndColumn(self.size):
            raise ValueError("Invalid shot. Shot coordinates not in range")
        elif self.board[coordinates.row][coordinates.column] < 0:
            raise ValueError("Invalid shot. You already shot there")

    def HasLost(self):
        has_won = True
        for i in self.board:
            for j in i:
                if j > 0:
                    has_won = False
                    break
        return has_won

    def UserShot(self, auto_play):
        if auto_play.lower() == "y":
            self.ComputerShot("user")
        else:
            has_shot = False
            while not has_shot:
                print("Write coordinates to shoot")
                user_shot_coordinates = Coordinates.Coordinates()
                try:
                    user_shot_coordinates.setRowAndColumn(
                        row=input(
                            f"Please write X coordinate to shoot . Max coordinate {self.size - 1} \r\n"
                        ),
                        column=input(
                            f"Please write Y coordinate to shoot. Max coordinate {self.size - 1} \r\n"
                        ),
                        max_len=self.size,
                    )
                    self.ValidateShot(user_shot_coordinates)
                    self.Shoot(user_shot_coordinates, "user")
                    has_shot = True
                except ValueError as error:
                    print(error)

    def ComputerShot(self, who_shot):
        has_shot = False
        while not has_shot:
            try:
                computer_shot_coordinates = Coordinates.Coordinates()
                computer_shot_coordinates.GenerateRandomRowAndColumn(self.size)
                self.ValidateShot(computer_shot_coordinates)
                self.Shoot(computer_shot_coordinates, who_shot=who_shot)
                has_shot = True
            except ValueError as error:
                has_shot = False

    @staticmethod
    def GetBoardPlan():
        return {"Ship shot": -2, "Missed": -1, "Empty": 0}
