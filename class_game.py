from class_check import *
from class_field import *


class Game:
    def player_step(self):
        while 1 == 1:
            if Check.draw(0):
                print('Ничья.')
                break
            number = input(
                'Ход крестиков, укажите доступную цифру для хода: ', )
            while not Check.move(number):
                number = input(
                    'Ход крестиков, укажите доступную цифру для хода: ', )
            number = int(number)
            Field.board[number - 1] = Field.X
            if Check.win(0):
                Field.board_output(0)
                break
            Game.computer_step(0)
            if Check.win(0):
                break
            if Check.draw(0):
                Field.board_output(0)
                print('Ничья.')
                break

    def computer_step(self):
        j, k = 0, 0
        pars = Field.win_vectors(0)
        cs = 0
        while j < len(pars):
            if pars[j].count(Field.X) < 1 \
                    and pars[j].count(Field.O) > 1 and not cs:
                while k < len(pars[j]):
                    if pars[j][k] != Field.O:
                        Field.board[Field.win_coordinates[j][k]] = Field.O
                        return(Field.win_coordinates[j][k])
                        cs = 1
                        break
                    k = k + 1
            j = j + 1
        j, k = 0, 0
        while j < len(pars):
            if pars[j].count(Field.X) > 1 \
                    and pars[j].count(Field.O) < 1 and not cs:
                while k < len(pars[j]):
                    if pars[j][k] != Field.X:
                        Field.board[Field.win_coordinates[j][k]] = Field.O
                        return(Field.win_coordinates[j][k])
                        cs = 1
                        break
                    k = k + 1
            j = j + 1
        if Field.board[0] == Field.X and Field.board[8] == Field.X \
                and Field.board[1] != Field.O \
                and Field.board[1] != Field.X and not cs:
            Field.board[1] = Field.O
            return(1)
            cs = 1
        if Field.board[2] == Field.X and Field.board[6] == Field.X \
                and Field.board[7] != Field.O \
                and Field.board[7] != Field.X and not cs:
            Field.board[7] = Field.O
            return(7)
            cs = 1
        if Field.board[4] == Field.O or Field.board[4] == Field.X and not cs:
            if Field.board[0] != Field.X \
                    and Field.board[0] != Field.O and not cs:
                Field.board[0] = Field.O
                return(0)
                cs = 1
            if Field.board[2] != Field.X \
                    and Field.board[2] != Field.O and not cs:
                Field.board[2] = Field.O
                return(2)
                cs = 1
            if Field.board[6] != Field.X \
                    and Field.board[6] != Field.O and not cs:
                Field.board[6] = Field.O
                return(6)
                cs = 1
            if Field.board[8] != Field.X \
                    and Field.board[8] != Field.O and not cs:
                Field.board[8] = Field.O
                return(8)
                cs = 1
        if Field.board[4] != Field.O \
                and Field.board[4] != Field.X and not cs:
            Field.board[4] = Field.O
            return(4)
            cs = 1
        if not cs:
            for i in range(len(Field.board)):
                if Field.board[i] in [1, 2, 3, 4, 5, 6, 7, 8, 9] and not cs:
                    Field.board[i] = Field.O
                    return(i)
                    cs = 1
        print('Ход ноликов:')
        Field.board_output(0)
