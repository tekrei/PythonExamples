#!/usr/bin/env python 
# coding=UTF-8
'''
A simple experimental RSS reader

First version: 12 Aug 2009
Upgrade to GTK3: 27 Mar 2016
'''
import sys
from RSSReader import *
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
    
class RSSReaderGTK:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("rssreader.glade") 
        dic = { "onLstRSSActivated" : self.onLstRSSActivated,
                "mainWindowDestroy" : self.mainWindowDestroy,
                "onBtnCopyClicked": self.onBtnCopyClicked,
                "onBtnExitClicked": self.mainWindowDestroy
        }
        self.builder.connect_signals(dic)
        self.lstRSS = self.builder.get_object("lstRSS")
        self.txtNews = self.builder.get_object("txtNews")
        self.rssOkuyucu = RSSReader('http://www.theguardian.com/world/rss')
        self.prepareList()
    
    def onBtnCopyClicked(self, widget):
        tb = self.txtNews.get_buffer()
        start_iter = tb.get_start_iter()
        end_iter = tb.get_end_iter()
        text = tb.get_text(start_iter, end_iter, True) 
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clipboard.set_text(text, -1)
    
    def mainWindowDestroy(self, widget):
        Gtk.main_quit()
    
    def onLstRSSActivated(self, widget, row, column):
        self.showSelectedNews(row)
    
    def showSelectedNews(self,row):
        textbuffer = self.txtNews.get_buffer()
        selectedNews = self.haberler[row[0]]
        text = selectedNews.description+"\n"+"<a href=\""+selectedNews.link+"\">"+selectedNews.link+"</a>"
        textbuffer.set_text(text)
    
    def populateNews(self):
        self.liststore.clear()
        self.haberler = self.rssOkuyucu.getItems()
        self.liststore.clear()
        for haber in self.haberler:
            self.liststore.append([haber.channel, haber.title])

    def prepareList(self):
        self.lstRSS.set_headers_visible(True)
        column = Gtk.TreeViewColumn("Source", Gtk.CellRendererText(), text=0)
        self.lstRSS.append_column(column)
        column = Gtk.TreeViewColumn("Title", Gtk.CellRendererText(), text=1)
        self.lstRSS.append_column(column)
        self.liststore = Gtk.ListStore(str, str)
        self.lstRSS.set_model(self.liststore)
        self.lstRSS.show()
        self.populateNews()

if __name__ == "__main__":
    hwg = RSSReaderGTK()
    Gtk.main()
