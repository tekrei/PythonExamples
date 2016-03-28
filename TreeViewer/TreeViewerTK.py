#!/usr/bin/env python
# coding=UTF-8
'''
tkinter kullanan ve dizindeki ogeleri listeyen oldukca basit bir uygulama
'''
from Tkinter import *
import os

class FileUtilities:
    "Once dizindeki dosyalari listeleyelim"
    "Her dosyanin boyutunu bulalim"
    def listDirectory(self,directory,fileExtList=None):
        "Verilen dizindeki ilgili extensiona sahip dosyalari donduruyor"
        "Eger bir uzanti verilmemisse tum dosyalari donduruyor"
        "Dizinler default olarak donduruluyor"
        fileList = [os.path.join(directory,f)
                        for f in os.listdir( directory )]           
        if(fileExtList is not None):
            fileList = [os.path.join( directory, f ) 
                       for f in fileList
                        if os.path.splitext( f )[1] in fileExtList] 
        return fileList
    
    def size(self,folder):
        "Verilen dizindeki dosyalarin (dizinlerde dahil) boyutlarini"
        "donduruyor. Ozyinelemeli olarak alt dizinleri tariyor"
        size = 0;
        if(self.isFolder(folder)):
            for file in self.listDirectory(folder):
                if(os.path.islink(file)==False):
                    size = size+self.size(file)
        else:
            if(os.path.islink(folder)==False):
                size = os.path.getsize(folder)
        return size
    
    def isFolder(self,directory):
        return os.path.isdir(directory)
    
    def currentDirectory(self):
        return os.path.curdir

class App:

    def __init__(self, master):

        self.fileUtilities = FileUtilities()
        self.frame = Frame(master)
        self.frame.pack()

        self.button = Button(self.frame, text="Çıkış", fg="red", command=self.frame.quit)
        self.button.pack(side=TOP)
        
        #Dizinleri ve boyutlarini sirasiyla gosterelim
        #Tiklanan dizinin alt dizinleri gosterilmeli
        #Once bulundugumuz dizini almaliyiz
        self.showDirectoryContents(".")

    def showDirectoryContents(self,directory):
        for file in self.fileUtilities.listDirectory(directory):
            size = self.fileUtilities.size(file)
            if self.fileUtilities.isFolder(file):
                self.name = Button(self.frame,text=str(file+" ("+str(size)+")"),command=self.showDirectoryContents(file))
                self.name.pack()
            else:
                self.name = Label(self.frame,text=str(file+" ("+str(size)+")"))
                self.name.pack()

root = Tk()

app = App(root)

root.mainloop()
