from class_field import *


class Check:
    def win(self):
        vect = Field.win_vectors(0)
        j = 0
        while j < len(vect):
            if vect[j].count(Field.X) == 3 or vect[j].count(Field.O) == 3:
                return Field.win_coordinates[j]
            else:
                j = j + 1
        else:
            return False

    def draw(self):
        vect = Field.win_vectors(0)
        while 1 == 1:
            number = 0
            for i in range(len(vect)):
                if vect[i].count(Field.X)>0 and vect[i].count(Field.O)>0:
                    number+=1
            if number == 8:
                return True
            if not any(e in range(len(Field.board) + 1) for e in Field.board):
                return True
            else:
                return False
