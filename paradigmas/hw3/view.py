class View:
    def display_board(self, board):
        print(" " + board[0] + " | " + board[1] + " | " + board[2])
        print("-----------")
        print(" " + board[3] + " | " + board[4] + " | " + board[5])
        print("-----------")
        print(" " + board[6] + " | " + board[7] + " | " + board[8])

    def display_result(self, result):
        if result == 'X':
            print("Игрок X победил!")
        elif result == 'O':
            print("Игрок O победил!")
        else:
            print("Ничья!")