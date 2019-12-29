class Field:
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win_coordinates = [[0, 1, 2], [0, 4, 8], [0, 3, 6],
                       [1, 4, 7], [2, 5, 8], [2, 4, 6],
                       [3, 4, 5], [6, 7, 8]]
    X = '\033[92m' + 'X' + '\033[0m'
    O = '\033[91m' + 'O' + '\033[0m'
    # '\033[92m' - зеленый цвет
    # '\033[91m' - красный цвет
    # '\033[0m' - конец цвета

    def win_vectors(self):
        return [[Field.board[0], Field.board[1], Field.board[2]],
                [Field.board[0], Field.board[4], Field.board[8]],
                [Field.board[0], Field.board[3], Field.board[6]],
                [Field.board[1], Field.board[4], Field.board[7]],
                [Field.board[2], Field.board[5], Field.board[8]],
                [Field.board[2], Field.board[4], Field.board[6]],
                [Field.board[3], Field.board[4], Field.board[5]],
                [Field.board[6], Field.board[7], Field.board[8]]]

    def board_output(self):
        i = 0
        while i < 8:
            print(Field.board[i], Field.board[i + 1], Field.board[i + 2])
            i = i + 3
