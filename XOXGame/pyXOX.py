#!/usr/bin/env python
# coding=UTF-8

'''
An *unfinished* GTK based Tic Tac Toe game

Upgrade to GTK3: 27 Mar 2016
'''
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys
import os

running_path = os.path.dirname(os.path.realpath(__file__))


class pXOX:

    def destroy(self, widget):
        Gtk.main_quit()

    def clickResult(self):
        result = "O"
        if(self.nextPlayer == 0):
            result = "X"
        return result

    def changePlayer(self):
        if(self.nextPlayer == 0):
            self.nextPlayer = 1
        else:
            self.nextPlayer = 0

    def winner(self):
        if(self.nextPlayer == 0):
            return "human"
        else:
            return "computer"

    def endGame(self):
        if(len(self.clicked) == 9):
            print("deuce!!!")

    def buttonClicked(self, widget):
        objectName = Gtk.Buildable.get_name(widget)
        if not objectName in self.clicked:
            self.clicked[objectName] = self.clickResult()
            widget.set_label(self.clicked[objectName])
            self.endGame()
            self.changePlayer()

    def __init__(self):

        self.nextPlayer = 0
        self.clicked = {}

        self.builder = Gtk.Builder()
        self.builder.add_from_file(running_path+"/pyxox.glade")

        self.dic = {}
        self.dic["on_cikis_clicked"] = self.destroy
        self.dic["destroyMain"] = self.destroy
        for i in range(3):
            for k in range(3):
                self.dic["on_"+str(i)+str(k)+"_clicked"] = self.buttonClicked
        self.builder.connect_signals(self.dic)
        Gtk.main()


if __name__ == "__main__":
    hwg = pXOX()
