#!/usr/bin/env python
# coding=UTF-8
'''
A simple experimental browser which also stores sites and categories in the DB

First version: 12 Aug 2009
Upgrade to GTK3: 27 Mar 2016
'''
import sys
from BrowserUtility import *
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('WebKit', '3.0')
from gi.repository import WebKit

class BrowserGTK:
    def __init__(self):
        self.webkit = WebKit.WebView()
        self.utility = Utility()
        self.builder = Gtk.Builder()
        self.builder.add_from_file("browser.glade")
        handlers = {
            "destroyWindow": self.destroy,
            "onBtnRemoveSiteClicked": self.onBtnRemoveSiteClicked,
            "onBtnAddSiteClicked": self.onBtnAddSiteClicked,
            "onCmbCategoriesChanged": self.onCmbCategoriesChanged,
            "onLstSitesRowActivated": self.onLstSitesRowActivated
        }
        self.builder.connect_signals(handlers)

        self.lstSites = self.builder.get_object("lstSites")
        self.cmbCategories = self.builder.get_object("cmbCategories")
        self.scrBrowser = self.builder.get_object("scrBrowser")
        self.prepareList()
        self.window = self.builder.get_object("mainWindow")
        self.window.show_all()
        Gtk.main()
        
    def destroy(self, widget):
        Gtk.main_quit()
        
    def onBtnRemoveSiteClicked(self,widget):
        model, rows = self.lstSites.get_selection().get_selected_rows()
        if len(rows) < 1:
            return None
        selectedSite = rows[0][0]
        if selectedSite:
            selected = self.sites[selectedSite]
            self.utility.removeSite(selected.url)
        self.populateSites(self.cmbCategories.get_active()+1)    

    def onBtnAddSiteClicked(self,widget):
        name = self.askInfo("Please enter site name", "Site name")
        url = self.askInfo("Please enter site URL", "Site URL")
        category = self.cmbCategories.get_active()+1
        if name and url and category>0:
            self.utility.addSite(name, url, category)
        self.populateSites(category)
    
    def onCmbCategoriesChanged(self,widget):
        self.populateSites(self.cmbCategories.get_active()+1)

    def responseToDialog(self, entry, dialog, response):  
        dialog.response(response)

    def askInfo(self, message, what):
        dialog = Gtk.MessageDialog(self.window,
            Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT ,
            Gtk.MessageType.QUESTION,
            Gtk.ButtonsType.OK,None)
        dialog.set_property("text",message)
        entry = Gtk.Entry()
        entry.connect("activate", self.responseToDialog, dialog, Gtk.ResponseType.OK)
        hbox = Gtk.HBox()
        hbox.pack_start(Gtk.Label(what), False, 5, 5)
        hbox.pack_start(entry, False, 5, 5)
        dialog.vbox.pack_start(hbox, False, 5, 5)
        dialog.show_all()
        dialog.run()
        returnValue = entry.get_text()
        dialog.destroy()
        return returnValue

    def onLstSitesRowActivated(self, widget, row, column):
        self.selectedSite = row
        self.showSite(row)
    
    def showSite(self,row):
        self.webkit.open(self.sites[row[0]].url)
    
    def populateSites(self,secili):
        self.sites = self.utility.getSites(secili)
        self.liststore.clear()
        for site in self.sites:
            self.liststore.append([site.name])

    def populateLists(self):
        liststore = Gtk.ListStore(str)
        cell = Gtk.CellRendererText()
        self.cmbCategories.pack_start(cell, True)
        self.cmbCategories.add_attribute(cell, 'text', 0)  
        for liste in self.utility.getCategory():
            liststore.append(liste)
        self.cmbCategories.set_model(liststore)

    def prepareList(self):
        column = Gtk.TreeViewColumn("Sites", Gtk.CellRendererText(), text=0)
        self.lstSites.append_column(column)
        self.liststore = Gtk.ListStore(str)
        self.lstSites.set_model(self.liststore)
        self.lstSites.show()
        self.populateLists()
        self.scrBrowser.add(self.webkit)
        self.webkit.show()

if __name__ == "__main__":
    hwg = BrowserGTK()
