# coding=UTF-8

import os
from tkinter import Tk, StringVar, Button, mainloop, Menu, messagebox
from PIL import ImageTk

running_path = os.path.dirname(os.path.realpath(__file__))


class BoardButton():
    def __init__(self, i, master=None):
        self.number = i
        self.row = int(i / 3)
        self.column = int(i % 3)
        self.text = StringVar()
        self.text.set("")

        def clicked():
            player(self.number)
        self.view = Button(master, textvariable=self.text, command=clicked,
                           bg='gray', width=200, height=150, image=empty_face)
        self.view.grid(row=self.row, column=self.column)


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
buttons = []
root = Tk()
empty_face = ImageTk.PhotoImage(file=running_path+"/empty.png")
green_face = ImageTk.PhotoImage(file=running_path+"/green.png")
yellow_face = ImageTk.PhotoImage(file=running_path+"/yellow.png")


def start(_buttons=buttons):
    board[:] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    _buttons = list(range(9))
    for i in range(9):
        _buttons[i] = BoardButton(i, master=root)
    buttons[:] = _buttons


def check_winner(player=21, _board=board):
    for c in range(3):
        if _board[0][c] + _board[1][c] + _board[2][c] == player:
            return True
    for r in range(3):
        if _board[r][0] + _board[r][1] + _board[r][2] == player:
            return True
    if _board[0][0] + _board[1][1] + _board[2][2] == player:
        return True
    if _board[0][2] + _board[1][1] + _board[2][0] == player:
        return True
    return False


def show_message_and_start(message):
    messagebox.showinfo("END OF GAME", message)
    start()


def check_end_game(b=board):
    if check_winner(player=15):
        show_message_and_start("You win! Congratulations!")
    elif check_winner():
        show_message_and_start("You lost!!!")


def check_board():
    for r in range(3):
        for c in range(3):
            if(board[r][c] == 0):
                return False
    return True


def player(x, b=board):
    r = int(x / 3)
    c = int(x % 3)
    if b[r][c] == 0:
        b[r][c] = 5
        set_button(x, 0)
        check_end_game()
        find_computer_move()
        if check_board():
            show_message_and_start("DEUCE!!!")
    else:
        messagebox.showerror("ERROR", "Wrong Move!")


def set_button(i, player):
    if player == 0:
        buttons[i].view.configure(image=green_face)
    else:
        buttons[i].view.configure(image=yellow_face)


def computer(r, c):
    board[r][c] = 7
    i = 3 * r + c
    set_button(i, 1)
    check_end_game()


def find_computer_move():
    empty_button = 0
    lost = 0
    board_copy = [board[0][:], board[1][:], board[2][:]]
    for c in range(3):
        for r in range(3):
            if board[r][c] == 0:
                board_copy[r][c] = 7
                if check_winner(_board=board_copy):
                    computer(r, c)
                    return
                else:
                    empty_button, satir, sutun = 1, r, c
                    board_copy[r][c] = 5
                    if check_winner(player=15, _board=board_copy):
                        lost, row1, column1 = 1, r, c
                    board_copy[r][c] = 0
    if lost:
        computer(row1, column1)
        return
    elif empty_button:
        computer(satir, sutun)
        return
    show_message_and_start("DEUCE!!!")


def main():
    root.title('XOX Game with Tkinter')

    menubar = Menu(root)
    menubar.add_command(label="NEW GAME", command=start)
    menubar.add_command(label="EXIT", command=root.quit)

    root.config(menu=menubar)
    start()
    mainloop()


if __name__ == "__main__":
    main()
