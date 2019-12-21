from GameBoard import GameBoard


def BattleShips():
    board_length = 9
    ships = {
        "Carrier": 5,
        "Battleship": 4,
        "Cruiser": 3,
        "Submarine": 3,
        "Destroyer": 2,
    }

    computer_board = GameBoard(size=board_length)

    player_board = GameBoard(size=board_length)

    computer_board.AddComputerShips(ships)

    player_board.AddUserShips(ships)
    auto_play = input("If you want to turn on autoplay, write: " "(Y)ES" "")
    while not (computer_board.HasLost() or player_board.HasLost()):
        computer_board.PrintBoard()
        player_board.PrintBoard(show_ships=True)
        player_board.UserShot(auto_play)
        computer_board.ComputerShot("computer")
    print(player_board.HasLost())
    print(computer_board.HasLost())
    if computer_board.HasLost():
        print("You won")
    else:
        print("You lost")


BattleShips()
