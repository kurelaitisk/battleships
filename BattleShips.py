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
    computer_board.add_ships_randomly(ships)
    player_board.add_ships_manually(ships)

    auto_play = input("If you want to turn on auto play, write: ""(Y)ES""")
    while not (computer_board.has_lost() or player_board.has_lost()):
        computer_board.print_board()
        player_board.print_board(show_ships=True)
        computer_board.manual_shot(auto_play)
        if computer_board.has_lost():
            break
        player_board.random_shot("computer")

    if computer_board.has_lost():
        print("You won")
    else:
        print("You lost")

    print("Game Over")


BattleShips()
