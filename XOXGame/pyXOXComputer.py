# coding=UTF-8

from Tkinter import Tk, StringVar, Button, mainloop, Menu
import tkMessageBox
from PIL import ImageTk

class BoardButton():
    def __init__(self, i, master=None):
        self.numara = i
        self.satir = i / 3
        self.sutun = i % 3
        self.metin = StringVar()
        self.metin.set("")
        def clicked():
            player(self.numara)
        self.view = Button(master, textvariable=self.metin , command=clicked, bg='gray', width=200, height=150, image=emptyFace)
        self.view.grid(row=self.satir, column=self.sutun)

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
buttons = []
root = Tk()
emptyFace = ImageTk.PhotoImage(file="RenksizAdam.png")
greenFace = ImageTk.PhotoImage(file="YesilAdam.png")
yellowFace = ImageTk.PhotoImage(file="SariAdam.png")

def start(_buttons=buttons):
    board[:] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    _buttons = range(9)
    for i in range(9):
        _buttons[i] = BoardButton(i, master=root)
    buttons[:] = _buttons

def winnerCheck(player=21, _board=board):
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

def showMessageAndStart(mesaj):
    tkMessageBox.showinfo("END OF GAME", mesaj)
    start()

def endGameCheck(b=board):
    if winnerCheck(player=15):
        showMessageAndStart("You win! Congratulations!")
    elif winnerCheck():
        showMessageAndStart("You lost!!!")

def checkBoard():
    for r in range(3):
        for c in range(3):
            if(board[r][c]==0):
                return False
    return True

def player(x, b=board):
    r = x / 3
    c = x % 3
    if b[r][c] == 0:
        b[r][c] = 5
        setButton(x,0)
        endGameCheck()
        findComputerMove()
        if checkBoard():
            showMessageAndStart("DEUCE!!!")
    else:
        tkMessageBox.showerror("ERROR", "Wrong Move!")

def setButton(i,kim):
    if kim==0:
        buttons[i].view.configure(image=greenFace)
    else:
        buttons[i].view.configure(image=yellowFace)

def computer(r, c):
    board[r][c] = 7
    i = 3 * r + c
    setButton(i,1)
    endGameCheck()
  
def findComputerMove():
    emptyButton = 0
    kayip = 0
    copyBoard = [board[0][:], board[1][:], board[2][:]]
    for c in range(3):
        for r in range(3):
            if board[r][c] == 0:
                copyBoard[r][c] = 7
                if winnerCheck(_board=copyBoard):
                    computer(r, c)
                    return
                else:
                    emptyButton, satir, sutun = 1, r, c
                    copyBoard[r][c] = 5
                    if winnerCheck(player=15, _board=copyBoard):
                        kayip , satir1, sutun1 = 1, r, c
                    copyBoard[r][c] = 0
    if kayip:
        computer(satir1, sutun1)
        return
    elif emptyButton:
        computer(satir, sutun)
        return
    showMessageAndStart("DEUCE!!!")

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
