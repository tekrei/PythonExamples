# coding=UTF-8

import os
# Tkinter is used for graphical interface
from tkinter import Tk, StringVar, Button, mainloop, Menu, Label, BOTTOM, Toplevel, Radiobutton, messagebox
from PIL import ImageTk

running_path = os.path.dirname(os.path.realpath(__file__))

# board information
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
buttons = []

# points
GREEN = 5
YELLOW = 7

# move
current_move = YELLOW

# player points
yellow_points = 0
green_points = 0


def start_game(_buttons=buttons):
    # clear board
    board[:] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # create buttons
    _buttons = list(range(9))
    for i in range(9):
        _buttons[i] = GameButton(i, master=root)
    buttons[:] = _buttons


def check_winner():
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]


def check_board():
    for r in range(3):
        for c in range(3):
            if(board[r][c] == 0):
                return False
    return True


def show_message_and_start(mesaj):
    messageBox.showinfo("End of Game", mesaj)
    baslat()


def check_endgame():
    winner = check_winner()
    if winner == YELLOW:
        show_message_and_start("YELLOW wins, Congratulations!")
        global yellow_points
        yellow_points += 1
    elif winner == GREEN:
        show_message_and_start("GREEN wins, Congratulations!")
        global green_points
        green_points += 1
    if check_board():
        show_message_and_start("DEUCE!!!")


def player(x):
    r = int(x / 3)
    c = int(x % 3)
    if board[r][c] == 0:
        board[r][c] = current_move
        set_button(x, current_move)
        check_endgame()
        next_move()
    else:
        messagebox.showerror("Error", "Wrong Move!")


def set_button(i, player):
    if player == GREEN:
        buttons[i].view.configure(image=green_icon)
    else:
        buttons[i].view.configure(image=yellow_icon)


def next_move():
    global current_move
    if current_move == GREEN:
        current_move = YELLOW
    else:
        current_move = GREEN


def points():
    exit_label = Tk()
    exit_label.title('Puan durumu')
    Label(exit_label, text='                 Puan Durumu                 ').pack(pady=15)
    Label(exit_label, text='YEŞİL:' + str(green_points)).pack(pady=15)
    Label(exit_label, text='YELLOW:' + str(yellow_points)).pack(pady=15)
    Button(exit_label, text="EXIT", command=exit_label.destroy).pack(side=BOTTOM)


class WhichColor:
    def yellow(self):
        self.v = YELLOW

    def green(self):
        self.v = GREEN

    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Pick your color").pack()
        self.top.transient(parent)

        self.v = 0

        rb1 = Radiobutton(top, text="Yellow", value=YELLOW,
                          command=self.yellow)
        rb1.pack()
        rb1.select()
        rb2 = Radiobutton(top, text="Green", value=GREEN, command=self.green)

        rb2.pack()
        rb2.deselect()

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global current_move
        current_move = self.v
        self.top.destroy()


class GameButton():
    def __init__(self, i, master=None):
        self.number = i
        self.row = int(i / 3)
        self.column = int(i % 3)
        self.text = StringVar()
        self.text.set("")

        def clicked():
            player(self.number)
        self.view = Button(root, command=clicked, bg='gray',
                           width=200, height=150, image=empty_icon)
        self.view.grid(row=self.row, column=self.column)


root = Tk()
root.wait_window(WhichColor(root).top)
root.title('XOX Graphical Interface')

menubar = Menu(root)
menubar.add_command(label="NEW GAME", command=start_game)
menubar.add_command(label="POINTS", command=points)
menubar.add_command(label="EXIT", command=root.quit)

root.config(menu=menubar)
empty_icon = ImageTk.PhotoImage(file=running_path+"/empty.png")
green_icon = ImageTk.PhotoImage(file=running_path+"/green.png")
yellow_icon = ImageTk.PhotoImage(file=running_path+"/yellow.png")
start_game()
mainloop()
