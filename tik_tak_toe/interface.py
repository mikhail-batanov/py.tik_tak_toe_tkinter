from class_field import *
from class_game import *
from tkinter import *
from class_check import *

window = Tk()
window.geometry('360x360')
window.title('Крестики-нолики')

w = 120
button_list = []
class Btn():
    global w, button_list
    def __init__(self, x0, y0, id):
        self.id = id
        self.x0 = x0
        self.y0 = y0
        self.Button1 = Button(bg = 'white',bd = 3)
        self.Button1.place(x=self.x0,y=self.y0,width=w,heigh=w)
        self.Button1.bind('<Button-1>',self.player_click)
        self.Button1.bind('',)

    def show(self):
        id = 0
        x = 0
        y = 0
        for i in range(3):
            for j in range(3):
                button_list.append(Btn(x,y, id))
                x += w
                id += 1
            x = 0
            y += w

    def computer(self, none):
        button_numb = Game.computer_step(0)
        button_list[button_numb].Button1.config(text = 'O', fg = 'red', font = ('Comic Sans MS', 24, 'bold'))
        button_list[button_numb].Button1.unbind('<Button-1>')

    def player_click(self, none):
        Field.board[self.id] = Field.X
        self.Button1.config(text = 'X', fg = 'green', font = ('Comic Sans MS', 24, 'bold'))
        self.Button1.unbind('<Button-1>')
        temp = Check.win(0)
        if temp != False:
            button_list[temp[0]].Button1.config(bg = '#ffff00')
            button_list[temp[1]].Button1.config(bg = '#ffff00')
            button_list[temp[2]].Button1.config(bg = '#ffff00')
        if Check.draw(0):
            for e in range(len(button_list)):
                button_list[e].Button1.config(bg = 'Grey')
                button_list[e].Button1.unbind('<Button-1>')
        self.computer(none)
        temp = Check.win(0)
        if temp != False:
            button_list[temp[0]].Button1.config(bg='#ffff00')
            button_list[temp[1]].Button1.config(bg='#ffff00')
            button_list[temp[2]].Button1.config(bg='#ffff00')
            for e in range(len(button_list)):
                button_list[e].Button1.unbind('<Button-1>')
        if Check.draw(0):
            for e in range(len(button_list)):
                button_list[e].Button1.config(bg='Grey')
                button_list[e].Button1.unbind('<Button-1>')
