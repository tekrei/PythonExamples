# coding=UTF-8

#Tkinter is used for graphical interface
from Tkinter import Tk, StringVar, Button, mainloop, Menu, Label, BOTTOM,Toplevel,Radiobutton
import tkMessageBox
from PIL import ImageTk

#board information
tahta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
buttons = []

#points
GREEN = 5
YELLOW = 7

#move
currentMove = YELLOW;

#player points
yellowPoints = 0;
greenPoints = 0;

def startGame(_buttons=buttons):    
    #clear board
    tahta[:] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #create buttons
    _buttons = range(9)
    for i in range(9):
        _buttons[i] = GameButton(i, master=root)
    buttons[:] = _buttons

def winCheck():
    for c in range(3):
        if tahta[0][c] == tahta[1][c] == tahta[2][c]:
            return tahta[0][c]
    for r in range(3):
        if tahta[r][0] == tahta[r][1] == tahta[r][2]:
            return tahta[r][0]
    if tahta[0][0] == tahta[1][1] == tahta[2][2]:
            return tahta[0][0]
    if tahta[0][2] == tahta[1][1] == tahta[2][0]:
            return tahta[0][2]

def checkBoard():
    for r in range(3):
        for c in range(3):
            if(tahta[r][c]==0):
                return False
    return True

def mesajGosterBaslat(mesaj):
    tkMessageBox.showinfo("Oyun Sonu", mesaj)
    baslat()

def endGameCheck():
    winner = winCheck()
    if winner == YELLOW:
        mesajGosterBaslat("YELLOW wins, Congratulations!")
        global yellowPoints
        yellowPoints += 1
    elif winner == GREEN:
        mesajGosterBaslat("GREEN wins, Congratulations!")
        global greenPoints
        greenPoints += 1
    if checkBoard():
        mesajGosterBaslat("DEUCE!!!")

def player(x):
    r = x / 3
    c = x % 3
    if tahta[r][c] == 0:
        tahta[r][c] = currentMove
        buttonSet(x, currentMove)
        endGameCheck()
        nextMove()
    else:
        tkMessageBox.showerror("Error", "Wrong Move!")

def buttonSet(i, kim):
    if kim == GREEN:
        buttons[i].gorunum.configure(image=yesilAdam)
    else:
        buttons[i].gorunum.configure(image=sariAdam)
     
def nextMove():
    global currentMove
    if currentMove == GREEN:
        currentMove = YELLOW
    else:
        currentMove = GREEN

def points():
    cikis = Tk()
    cikis.title('Puan durumu')
    Label(cikis, text='                 Puan Durumu                 ').pack(pady=15)
    Label(cikis, text='YEŞİL:' + str(greenPoints)).pack(pady=15)
    Label(cikis, text='YELLOW:' + str(yellowPoints)).pack(pady=15)
    Button(cikis, text="EXIT", command=cikis.destroy).pack(side=BOTTOM)

class WhichColor:
    def sari(self):
        self.v = YELLOW
    def yesil(self):
        self.v = GREEN
        
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Pick your color").pack()
        
        self.v = 0;

        rb1 = Radiobutton(top, text="Yellow",value=YELLOW,command=self.sari)
        rb1.pack()
        rb1.select()
        rb2 = Radiobutton(top, text="Green",value=GREEN,command=self.yesil)

        rb2.pack()
        rb2.deselect()
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global currentMove
        currentMove = self.v
        self.top.destroy()

class GameButton():
    def __init__(self, i, master=None):
        self.numara = i
        self.satir = i / 3
        self.sutun = i % 3
        self.metin = StringVar()
        self.metin.set("")
        def clicked():
            player(self.numara)
        self.gorunum = Button(root, command=clicked, bg='gray', width=200, height=150, image=renksizAdam)
        self.gorunum.grid(row=self.satir, column=self.sutun)

root = Tk()
root.wait_window(WhichColor(root).top)
root.title('XOX Graphical Interface')

menubar = Menu(root)
menubar.add_command(label="NEW GAME", command=startGame)
menubar.add_command(label="POINTS", command=points)
menubar.add_command(label="EXIT", command=root.quit)

root.config(menu=menubar)
renksizAdam = ImageTk.PhotoImage(file="RenksizAdam.png")
yesilAdam = ImageTk.PhotoImage(file="YesilAdam.png")
sariAdam = ImageTk.PhotoImage(file="SariAdam.png")
startGame()
mainloop()
